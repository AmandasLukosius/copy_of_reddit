from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

# Create your views here.

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['url']:
			post = Post()
			post.title = request.POST['title']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				post.url = request.POST['url']
			else:
				post.url = 'http://' + request.POST['url']
			post.pub_date = timezone.datetime.now()
			post.author = request.user
			post.save()
			return redirect('home')
		else:
			return render(request, 'posts/create.html', {'error':'ERROR: You must include a title and a URL to create a post.'})
	else:
		return render(request, 'posts/create.html')

def home(request):
	posts = Post.objects.order_by('-votes_total', '-pub_date')

	query = request.GET.get("q")
	if query:
		posts = posts.filter(
			Q(title__icontains=query) |
			Q(url__icontains=query) |
			Q(author__username__icontains=query)
			).distinct()

	post_numbers =  posts.count()

	return render(request, 'posts/home.html', {'posts':posts, 'post_numbers':post_numbers})

def upvote(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk=pk)
		post.votes_total += 1
		post.save()
		return redirect('home')

def downvote(request, pk):
	if request.method == 'POST':
		post = Post.objects.get(pk=pk)
		post.votes_total -= 1
		post.save()
		return redirect('home')

def userposts(request, pk):
	posts = Post.objects.filter(author__id=pk).order_by('-votes_total', '-pub_date')
	author = User.objects.get(pk=pk)
	return render(request, 'posts/userposts.html', {'posts':posts, 'author':author})
