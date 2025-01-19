from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def post_list(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/post.html', context)

@csrf_exempt # CSRF 토큰 검사를 하지 않음
def like_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX 요청 확인
        print("Request received")
        data = json.loads(request.body)  # JSON 데이터를 파싱
        post_id = data.get("id")
        like_type = data.get("type")

        if not post_id or not like_type:
            return JsonResponse({"error": "Invalid data"}, status=400)

        post = Post.objects.get(id=post_id)
        if like_type == "like":
            post.likes += 1
        elif like_type == "unlike":
            post.likes -= 1

        post.save()
        return JsonResponse({"id": post.id, "likes": post.likes, "liked": like_type == "like"})