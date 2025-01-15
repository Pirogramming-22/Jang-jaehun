from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea
from django.http import JsonResponse # 관심도 버튼 클릭 시 JSON 응답


def main(request):
    # ideas 테이블의 모든 레코드를 가져옴
    # ideas = Idea.objects.all() 
    sort = request.GET.get('sort', None) # GET 요청으로 sort 파라미터를 받아옴 # 기본값: None (정렬 안 함)

    if sort == 'popular':
        ideas = Idea.objects.all().order_by('-interest') # 찜하기순 - 내림차순으로 정렬
    elif sort == 'oldest':
        ideas = Idea.objects.all().order_by('id') # 등록순 - id 내림차순으로 정렬
    elif sort == 'newest':
        ideas = Idea.objects.all().order_by('-id') # 최신순 id 오름차순으로 정렬
    elif sort == 'name':
        ideas = Idea.objects.all().order_by('title') # 이름순 - 이름 오름차순으로 정렬
    else:
        ideas = Idea.objects.all() # 정렬 안 함

    context = {
        'ideas': ideas,
        'sort': sort,
    }
    # db의 모든 레코드를 가져와서 idea_list.html에 전달
    return render(request, 'ideas/idea_list.html', context)

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES) # 파일 업로드를 위해 request.FILES 추가
        if form.is_valid(): # 폼 유효성 검사
            form.save()
            return redirect('ideas:main')
    else:
        form = IdeaForm() # GET 요청시 빈 폼을 생성
    
    context = {
        'form': form
    }
    return render(request, 'ideas/idea_create.html', context)

def idea_detail(request, pk):
    idea = Idea.objects.get(pk = pk) # id가 pk인 레코드를 가져옴

    context = {
        'idea': idea
    }

    return render(request, 'ideas/idea_detail.html', context)

def idea_delete(request, pk):
    idea = Idea.objects.get(id = pk) # id가 pk인 레코드를 가져옴
    idea.delete() # 레코드 삭제

    return redirect('ideas:main')

def idea_update(request, pk):
    idea = Idea.objects.get(id = pk)  # 특정 아이디어 가져오기

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)  # instance=idea 추가
        if form.is_valid():  # 폼 유효성 검사
            # 이미지 삭제 체크박스 처리
            if 'remove_image' in request.POST and request.POST['remove_image'] == 'on':
                if idea.image:  # 이미지가 존재할 경우
                    idea.image.delete()  # 기존 이미지 삭제
                    idea.image = None  # 필드 초기화
            form.save()  # 수정된 레코드 저장
        else:
            print("Form is not valid.")
            print("Errors:", form.errors)
        return redirect('ideas:idea_detail', pk=pk)  # 수정 후 상세 페이지로 이동
    else:
        form = IdeaForm(instance=idea)  # GET 요청 시 기존 레코드의 값을 폼에 채워서 생성

    context = {
        'idea': idea,
        'form': form
    }
    return render(request, 'ideas/idea_update.html', context)

def interest_plus(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest += 1  # 관심도 증가
    idea.save()
    return redirect('ideas:main')  # 메인 페이지로 리디렉션 또는 적합한 페이지로 이동

def interest_minus(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if idea.interest > 0:  # 관심도가 음수로 내려가지 않도록 방어코드
        idea.interest -= 1  # 관심도 감소
        idea.save()
    return redirect('ideas:main')  # 메인 페이지로 리디렉션 또는 적합한 페이지로 이동