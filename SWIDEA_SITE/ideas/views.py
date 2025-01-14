from django.shortcuts import render, redirect
from .forms import IdeaForm
from .models import Idea

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
    idea = Idea.objects.get(pk=pk)
    context = {
        'idea': idea
    }

    return render(request, 'ideas/idea_detail.html', context)