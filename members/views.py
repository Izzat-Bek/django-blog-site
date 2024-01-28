from django.shortcuts import render, redirect
from .forms import SignUpForm, UserCreateProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, StarModel
from django.contrib.auth.decorators import login_required
from blog.models import PostModel



def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request, 'members/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'members/login.html', {'form': form})

@login_required
def logout_request(request):
    logout(request)
    return redirect('home')
    
@login_required
def create_profile_view(request, id_user):
    # Get the user object based on the given id
    user = User.objects.get(id=id_user)
    auth = False
    if user == request.user:
        auth = True
    else:
        auth = False
    if request.method == 'POST':
        # Create a form object with the POST data and files
        form = UserCreateProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Create a profile object from the form data, but don't save it yet
            profile = form.save(commit=False)
            
            # Set the user attribute of the profile to the current user
            profile.user = user
            
            # Save the profile object in the database
            profile.save()
            
            # Redirect the user to the home page
            return redirect('home')
    else:
        # Create a form object without any data
        form = UserCreateProfileForm()
    
    # Render the create profile template with the form object
    return render(request, 'members/create_profile.html', {'form': form, 'auth': auth})


@login_required
def edit_profile_view(request, id_user):
    profile = Profile.objects.get(id=id_user)
    user = profile.user
    auth = False
    if user == request.user:
        auth = True
    else:
        auth = False
        
    if request.method == 'POST':
        form = UserCreateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        initial_data = {field.name: getattr(profile, field.name) for field in Profile._meta.fields}
        form = UserCreateProfileForm(initial=initial_data)
    return render(request, 'members/edit_profile.html', {'form': form, 'auth': auth})



def profile_view(request, id_user):
    profile = Profile.objects.get(id=id_user)
    user = User.objects.get(id=request.user.id)
    prof_acc = Profile.objects.get(user=user)
    liked = False
    if profile.likes.filter(id=profile.id).exists():
        liked = True
    star = StarModel.objects.filter(user_acc=profile)
    
    count = 0
    ball = 0
    for i in star:
        count += 1
        ball += i.star_num
    rat = 0
    if count == 0:    
        rat = 0
    else:
        rat = round(ball/count)
    
    rating = list(range(1, rat+ 1)) 
    unrating = list(range(rat + 1, 6))
    
    context = {
        'profile': profile,
        'liked': liked,
        'rating': rating,
        'unrating': unrating,
        'rat': rat,
        'ball': ball,
        'prof_acc': prof_acc,
    }
    
    return render(request, 'members/profile_view.html', context)


@login_required
def delete_profile(request, id_user):
    user = User.objects.get(id=id_user)
    profile = Profile.objects.get(user=user)
    profile.delete()
    return redirect('home')


@login_required
def like_view(request, id_user):
    profile = Profile.objects.get(id=id_user)
    liked = False
    if profile.likes.filter(id=profile.id).exists():
        profile.likes.remove(profile.id)
        liked = False
    else:
        profile.likes.add(profile.id)
        liked = True    
    return redirect('profile', id_user=id_user)


@login_required
def star_view(request, id_user, ball):
    ball = int(ball)
    profile_acc = Profile.objects.get(id=id_user)
    profile = Profile.objects.get(user=request.user)
    if StarModel.objects.filter(user_acc=profile_acc, user=profile).exists():
        star = StarModel.objects.get(user_acc=profile_acc, user=profile)
        star.star_num = ball
        star.save()
    else:
        star = StarModel.objects.create(user_acc=profile_acc, user=profile, star_num=ball)
        star.save()
        
    return redirect('profile', id_user=id_user)


def post_profile_accounts_view(request, id_prof):
    profile = Profile.objects.get(id=id_prof)
    post = PostModel.objects.filter(author=profile).order_by['-id']
    context = {
        'profile': profile,
        'post': post,
    }
    return render(request, 'members/post_profile_accounts.html', context)
