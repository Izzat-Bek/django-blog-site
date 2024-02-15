from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from members.models import Profile
from django.contrib.postgres.search import TrigramSimilarity
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Author', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Category')
    content1 = RichTextField(blank=True, null=True, verbose_name='Content')
    image1 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image', default='img/default/sport1.jpg')
    content2 = RichTextField(blank=True, null=True, verbose_name='Content')
    image2 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content3 = RichTextField(blank=True, null=True, verbose_name='Content')
    image3 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content4 = RichTextField(blank=True, null=True, verbose_name='Content')
    image4 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content5 = RichTextField(blank=True, null=True, verbose_name='Content')
    image5 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content6 = RichTextField(blank=True, null=True, verbose_name='Content')
    image6 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content7 = RichTextField(blank=True, null=True, verbose_name='Content')
    image7 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content8 = RichTextField(blank=True, null=True, verbose_name='Content')
    image8 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content9 = RichTextField(blank=True, null=True, verbose_name='Content')
    image9 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content10 = RichTextField(blank=True, null=True, verbose_name='Content')
    image10 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    content11 = RichTextField(blank=True, null=True, verbose_name='Content')
    image11 = models.ImageField(upload_to='images/post/', blank=True, null=True, verbose_name='Image')
    date_ad = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Profile, blank=True, related_name='post_likes', verbose_name='Likes')
    view_profile = models.ManyToManyField(Profile, blank=True, symmetrical=False, related_name='post_view_user', verbose_name='View')
    
    def __str__(self):
        return f'{self.title}'

    
    def total_likes(self):
        if self.likes.count() == 0 or self.likes.count() == 1:
            return f'{self.likes.count()} like'
        else:
            return f'{self.likes.count()} likes'
    
    
    def total_view(self):
        if self.view_profile.count() == 0 or self.view_profile.count() == 1:
            return f'{self.view_profile.count()} view'
        else:
            return f'{self.view_profile.count()} views'
    
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'id_post': self.id})
    
    
    
    @staticmethod
    def search_postgres(query):
        return PostModel.objects.annotate(similarity=TrigramSimilarity('title', query)).filter(similarity__gt=0.3).order_by('-similarity')

    @staticmethod
    def search(query):
        return PostModel.objects.filter(title__icontains=query).order_by('-date_ad')
    
    
    @staticmethod
    def sear_for_split(query):
        words = query.split()
        result = set()
        for word in words:
            result.add(PostModel.objects.filter(title__icontains=word).order_by('-date_ad'))
        return result
        
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    comment = models.CharField(blank=True, null=True, verbose_name='Comment', max_length=1000)
    date_ad = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.comment}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'    


class StarModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    star_num = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
