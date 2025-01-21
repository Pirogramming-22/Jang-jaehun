from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
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

@csrf_exempt
def post_comments(request, post_id):
    try:
        post = Post.objects.get(id=post_id)

        if request.method == 'GET':
            # 댓글 조회
            comments = post.comments.all()
            if not comments.exists():
                return JsonResponse([], safe=False)  # 빈 배열 반환

            comments_data = [
                {   
                    'id': comment.id,
                    'user': comment.user,
                    'text': comment.text,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                }
                for comment in comments
            ]
            return JsonResponse(comments_data, safe=False)

        elif request.method == 'POST':
            # 댓글 추가
            data = json.loads(request.body)
            user_name = data.get('user')
            text = data.get('text')

            if not text:
                return JsonResponse({'error': '댓글 내용이 없습니다.'}, status=400)

            comment = Comment.objects.create(post=post, user=user_name, text=text)  # 사용자 처리 예시
            return JsonResponse({
                'id': comment.id,
                'user': comment.user,
                'text': comment.text,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
            })

        return JsonResponse({'error': 'Invalid request method'}, status=405)

    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def delete_comment(request, post_id, comment_id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(id=post_id)
            comment = Comment.objects.get(id=comment_id, post=post)
            comment.delete()
            return JsonResponse({'message': 'Comment deleted successfully.'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found.'}, status=404)
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)