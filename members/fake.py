from random import randint
from django.contrib.auth.models import User
from .models import Profile, StarModel
from faker import Faker
from django.conf import settings
import string

path = settings.BASE_DIR / 'media' / 'images' / 'account'
path_txt = settings.BASE_DIR / 'users.txt'


def create_user_fake(nums=100):
    ascii_table = string.ascii_letters + string.digits + string.punctuation
    fake = Faker()
    with open(path_txt, 'a') as file:
        for i in range(nums):
            password = ''.join([ascii_table[randint(0, len(ascii_table) - 1)] for _ in range(32)])
            username = fake.user_name()
            last_name = fake.last_name()
            first_name = fake.first_name()
            email = fake.email()        
            file.write(f'username -- {username}:                password -- {password} \n')
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            print(f'{i+1}[*]: -->  User {username} created')

            
        

def create_profile_fake(nums=100):
    users = User.objects.all()
    photo1 = ''
    fake = Faker()
    num = 0
    for user in users:
        num += 1
        bio = ' '.join(fake.sentence() for _ in range(randint(10, 30)))
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user, bio=bio)
            print(f'{num}[*] --> {user} Profile created')



def add_like(user='admin'):
    profile = Profile.objects.get(user__username=user)
    profiles = Profile.objects.all()
    for i in profiles:
        if profile.likes.filter(id=i.id).exists():
            pass
        else:
            profile.likes.add(i)


def add_star(user='admin'):
    profile = Profile.objects.get(user__username=user)
    profiles = Profile.objects.all()
    for i in profiles:
        if StarModel.objects.filter(user_acc=profile, user=i).exists():
            pass
        else:
            star = StarModel.objects.create(user_acc=profile, user=i, star_num=5)

    