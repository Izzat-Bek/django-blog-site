from .models import PostModel, Category
from random import randint
from django.contrib.auth.models import User
from faker import Faker
from members.models import Profile


def create_category_fake(nums=10):
    fake = Faker()
    for i in range(nums):
        name = str(fake.word())
        Category.objects.create(name=name)
        print(f'{i+1}[*] --> Category {name} created')


def create_post_fake(nums=100):
    authors = Profile.objects.all()
    fake = Faker()
    categories = Category.objects.all()    
    for i in range(nums):
        title = ' '.join(fake.word() for _ in range(randint(3, 10)))
        content1 = ' '.join(fake.sentence() for _ in range(randint(10, 30))) 
        author = authors[randint(0, len(authors) - 1)]
        cat = categories[randint(0, len(categories) - 1)]
        PostModel.objects.create(author=author, category=cat, title=title, content1=content1)
        print(f'{i+1}[*] --> Post {title} created')
    
    
def add_likes_to_post(id_post):
    profile = Profile.objects.all()
    post  = PostModel.objects.get(id=id_post)
    count_like = 0
    for i in profile:
        if post.likes.filter(id=i.id).exists():
            pass
        else:
            post.likes.add(i)
            count_like += 1
        
    return f'Adds {count_like} likes'