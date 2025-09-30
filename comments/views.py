from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

def comment_page(request):  # This is the missing view
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment_page.html', {'comments': comments})

@require_POST
@login_required
@csrf_exempt
def add_comment(request):
    try:
        data = json.loads(request.body)
        text = data.get('text', '').strip()
        
        if not text:
            return JsonResponse({'error': 'Comment cannot be empty'}, status=400)
            
        comment = Comment.objects.create(
            user=request.user,
            text=text,
            likes=0,
            dislikes=0
        )
        
        return JsonResponse({
            'id': comment.id,
            'user': comment.user.username,
            'text': comment.text,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
            'likes': comment.likes,
            'dislikes': comment.dislikes
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid request data'}, status=400)

@require_POST
@login_required
@csrf_exempt
def rate_comment(request, comment_id):
    try:
        data = json.loads(request.body)
        comment = Comment.objects.get(id=comment_id)
        
        if data.get('action') == 'like':
            comment.likes += 1
        elif data.get('action') == 'dislike':
            comment.dislikes += 1
            
        comment.save()
        
        return JsonResponse({
            'id': comment.id,
            'likes': comment.likes,
            'dislikes': comment.dislikes
        })
        
    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    

def get_new_comments(request):
    last_id = request.GET.get('last_id', 0)
    try:
        last_id = int(last_id)
    except ValueError:
        last_id = 0
    
    new_comments = Comment.objects.filter(id__gt=last_id).order_by('-id')[:10]
    
    comments_data = [{
        'id': c.id,
        'user': c.user.username,
        'text': c.text,
        'created_at': c.created_at.strftime('%Y-%m-%d %H:%M')
    } for c in new_comments]
    
    return JsonResponse({'comments': comments_data})