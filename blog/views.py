from django.shortcuts import render, redirect
from .models import PostModel, CommentModel, StarModel, Category
from django.contrib.auth.models import User
from .forms import AddCommentForm, AddCommentFormUsername, SearchForm, AddPost
from members.models import Profile
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from time import time


def url_address(request):
    return f'http://{get_current_site(request).domain}:{request.META["SERVER_PORT"]}'


def base_home(request, id_cat):
    post = None
    if id_cat is None:
        post = PostModel.objects.all().order_by('-date_ad')
    else:
        category = Category.objects.get(id=id_cat)
        post = PostModel.objects.filter(category=category).order_by('-date_ad')
    
    user_profile = True
    profile = None
    liked = None
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            user_profile = False
            post1 = PostModel.objects.filter(likes=profile)
            liked = [i.id for i in post1]
        else:
            user_profile = True

    else:
        user_profile = True
    context = {
        'post': post,
        'user_profile': user_profile,
        'profile': profile,
        'liked': liked,
    }
    
    paginator = Paginator(post, 16)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    
    results = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query', '').strip()
            if query:
                time1 = time()
                context['query'] = query
                results = PostModel.search_postgres(query=query)
                
                if not results:
                    results = PostModel.search(query=query)
                time2 = time()
                times = round(time2 - time1, 2)
                context['times'] = times
                paginator_result = Paginator(results, 16)
                page_number_result = request.GET.get("page")
                results1 = paginator_result.get_page(page_number_result)
                
                context['results'] = results
                context['results1'] = results1
                context['page_result'] = results1
                context['page_count_result'] = paginator_result.num_pages
                context['paginator_result'] = paginator_result
    
    else:
        form = SearchForm()
    
    
    context['form'] = form
    context['page'] = page
    context['page_count'] = paginator.num_pages
    context['paginator'] = paginator
    return context

    

def home_view(request):
    URL_ADD = url_address(request)
    context = base_home(request, None)
    return render(request, 'blog/home.html', context)

    
def category_view(request, id_cat):
    context = base_home(request, id_cat)
    return render(request, 'blog/home.html', context)


def article_detail(request, id_post):
    post = PostModel.objects.get(id=id_post)
    star = StarModel.objects.filter(post=id_post)
    user_acc = None
    profile = None
    liked = False
    form_user = None
    form = None
    if request.user.is_authenticated:
        user_acc = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user_acc)
        
        if not post.view_profile.filter(id=profile.id).exists():
            post.view_profile.add(profile)

        if post.likes.filter(id=profile.id).exists():
            liked = True        
    
    
    count = star.count()
    ball = sum([i.star_num for i in star])
    
    rat = 0
    rat1 = 0
    if count == 0:    
        rat = 0
    
    else:
        rat1 = round(ball/count, 1)
        rat = round(ball/count)
    comment = CommentModel.objects.filter(post=id_post)
    rating = list(range(1, rat+ 1))
    unrating = list(range(rat + 1, 6))
    context = {
        'post': post,
        'rating': rating,
        'comment': comment,
        'count': count,
        'ball': ball,
        'liked': liked,
        'unrating': unrating,
        'rat': rat,
        'rat1': rat1,
        'profile': profile,
        'form': form,
        'form_user': form_user,
    }    
    return render(request, 'blog/article.html', context)


def add_star(request, id_post, ball):
    ball = int(ball)
    post = PostModel.objects.get(id=id_post)
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    
    if StarModel.objects.filter(post=post, profile=profile).exists():
        star = StarModel.objects.get(post=post, profile=profile)
        star.star_num = ball
        star.save()
    else:
        star = StarModel.objects.create(post=post, profile=profile, star_num=ball)
        star.save()
    return redirect('article', id_post=id_post)


def comment_view(request, id_post, id_user):
    from crispy_forms.utils import render_crispy_form
    
    
    post = PostModel.objects.get(id=id_post)
    messages = None
    if request.method == 'POST' and  request.is_ajax():
        form = AddCommentFormUsername(request.POST)
        if form.is_valid():
            username = User.objects.get(id=id_user).username
            comment= form.cleaned_data['comment']
            comment1 = CommentModel.objects.create(post=post, username=username, comment=comment)
            comment1.save()
            message = 'Ваш комментарий успешно добавлен'
            return JsonResponse({'message': message, 'success': True})
        else:
            messages = 'Ваш комментарий не добавлен'
            return JsonResponse({'message': messages, 'success': False})
    else:
        form = AddCommentFormUsername()
        form_html = render_crispy_form(form)
    return JsonResponse({'form_html': form_html, 'post': post})


def comment_username_view(request, id_post):
    post = PostModel.objects.get(id=id_post)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            comment = form.cleaned_data['comment']
            comment1 = CommentModel.objects.create(post=post, comment=comment, username=username)
            comment1.save()
            return redirect('article', id_post=post.id)
    else:
        form = AddCommentForm()
    post = PostModel.objects.get(id=id_post)
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})
  
  
def like_view_jquere(request, post_id):
    id_post = post_id
    post = PostModel.objects.get(id=id_post)
    user_acc = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user_acc)
    
    liked = False
    if post.likes.filter(id=profile.id).exists():
        post.likes.remove(profile.id)
        liked = False
    else:
        post.likes.add(profile.id)
        liked = True
    count = post.total_likes()
    return JsonResponse({'liked': liked, 'likes_count': count})



def like_home_view_jquere(request, post_id):
    post = PostModel.objects.get(id=post_id)
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    if post.likes.filter(id=profile.id).exists():
        post.likes.remove(profile.id)
    else:
        post.likes.add(profile.id)
    post1 = PostModel.objects.filter(likes=profile)
    liked = [i.id for i in post1]    
    return JsonResponse({'liked': liked, 'likes_count': post.total_likes()})


def delete_post_view(request, id_post):
    post = PostModel.objects.get(id=id_post)
    post.delete()
    return redirect('home')


def contact_view(request):
    
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    if 'query' in request.method:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = User.objects.filter(username__icontains=query)
            context['results'] = results
    else:
        form = SearchForm()
    
    context['form'] = form
    return render(request, 'blog/contacts.html', context)


def add_post_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('home')
    else:
        form = AddPost()
    return render(request, 'blog/add_post.html', {'form': form})