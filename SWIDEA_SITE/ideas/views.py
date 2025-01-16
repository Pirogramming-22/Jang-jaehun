from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea, IdeaStar
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
    
    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    # 현재 세션에 대해 찜된 아이디어의 ID를 가져옴
    starred_ideas = IdeaStar.objects.filter(session_key=session_key).values_list('idea_id', flat=True)

    context = {
        'ideas': ideas,
        'sort': sort,
        'starred_ideas': list(starred_ideas),  # 찜한 아이디어 목록 전달
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
    # IdeaStar 테이블에서 현재 아이디어가 찜 되었는지 확인
    ideastar = IdeaStar.objects.filter(idea=idea).exists()

    context = {
        'idea': idea,
        'ideastar': ideastar,
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

# 찜하기 기능
# def toggle_star(request, pk):
#     idea = get_object_or_404(Idea, pk=pk)
#     session_key = request.session.session_key

#     if not session_key:
#         # 세션이 없으면 생성
#         request.session.create()
#         session_key = request.session.session_key

#     # IdeaStar의 존재 여부 확인 및 토글 처리
#     try:
#         star, created = IdeaStar.objects.get_or_create(idea=idea, session_key=session_key)
#         if not created:
#             # 이미 존재하면 삭제
#             star.delete()
#             return JsonResponse({'success': True, 'starred': False})
#         return JsonResponse({'success': True, 'starred': True})
#     except IntegrityError:
#         return JsonResponse({'success': False, 'error': 'Database error'})

def toggle_star(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)

        # 현재 사용자는 없는 경우 익명 사용자 처리
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        # 찜 상태 확인
        star, created = IdeaStar.objects.get_or_create(idea=idea, session_key=session_key)

        if not created:  # 이미 찜한 경우 -> 삭제
            star.delete()
            return JsonResponse({'success': True, 'starred': False})

        # 새롭게 찜한 경우
        return JsonResponse({'success': True, 'starred': True})

    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'})

# 관심도 버튼 클릭 시 관심도 증가
def interest_plus(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.interest += 1
    idea.save()
    return JsonResponse({'success': True, 'interest': idea.interest})

# 관심도 버튼 클릭 시 관심도 감소
def interest_minus(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if idea.interest > 0:
        idea.interest -= 1
        idea.save()
    return JsonResponse({'success': True, 'interest': idea.interest})