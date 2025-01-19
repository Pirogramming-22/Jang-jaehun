from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def post_list(request):

    posts = Post.objects.all()

    for post in posts:
        post.is_liked = post.likes > 0  # likes가 0보다 크면 liked 상태

    context = {
        'posts': posts
    }

    return render(request, 'post/post.html', context)

@csrf_exempt # CSRF 토큰 검사를 하지 않음
def like_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get("id")
        post = Post.objects.get(id=post_id)

        # likes 값 토글 (0 -> 1, 1 -> 0)
        post.likes = 1 if post.likes == 0 else 0
        post.save()

        return JsonResponse({
            "id": post.id,
            "likes": post.likes,
            "liked": post.likes == 1
        })