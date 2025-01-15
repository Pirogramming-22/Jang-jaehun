from django.shortcuts import render, redirect
from .forms import DevtoolForm
from .models import Devtool

# Create your views here.

def main(request):
    devtools = Devtool.objects.all()

    context = {
        'devtools': devtools
    }

    return render(request, 'devtools/dev_list.html', context)

def devtool_create(request):
    if request.method == 'POST':
        form = DevtoolForm(request.POST, request.FILES) # 파일 업로드를 위해 request.FILES 추가
        if form.is_valid(): # 폼 유효성 검사
            form.save()
            return redirect('devtools:main')
    else: # GET 요청시 빈 폼을 생성
        form = DevtoolForm()

    context = {
        'form': form
    }
    return render(request, 'devtools/dev_create.html', context)

def devtool_detail(request, pk):
    devtool = Devtool.objects.get(id = pk) # id가 pk인 레코드를 가져옴

    context = {
        'devtool': devtool
    }

    return render(request, 'devtools/dev_detail.html', context)

def devtool_delete(request, pk):
    devtool = Devtool.objects.get(id = pk) # id가 pk인 레코드를 가져옴
    devtool.delete() # 레코드 삭제

    return redirect('devtools:main')

def devtool_update(request, pk):
    devtool = Devtool.objects.get(pk = pk)  # 특정 아이디어 가져오기

    if request.method == 'POST':
        form = DevtoolForm(request.POST, request.FILES, instance=devtool) # 파일 업로드를 위해 request.FILES 추가
        if form.is_valid(): # 폼 유효성 검사
            form.save()
            return redirect('devtools:devtool_detail', pk=pk)
    else: # GET 요청시 빈 폼을 생성
        form = DevtoolForm(instance=devtool)

    context = {
        'form': form,
        'devtool': devtool
    }
    return render(request, 'devtools/dev_update.html', context)