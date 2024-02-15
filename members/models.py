import os
from io import BytesIO
from random import randint

from PIL import Image, ImageDraw, ImageFont
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

path = settings.BASE_DIR / 'media' / 'images' / 'account'

path_image = settings.BASE_DIR / 'media' / 'profile' / 'Image'


def generate_random_image(width=500, height=500, name_image='image.JPEG'):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    image = Image.new(mode='RGB', size=(width, height), color=color)
    image.save(f'{path}/{name_image}.JPEG')
    return f'{path / name_image}.JPEG'


def add_word_to_image(input_image=None, letter='A'):
    image = Image.open(input_image)
    draw = ImageDraw.Draw(image)
    path_to_font = settings.BASE_DIR / 'static' / 'font' / 'sfns-display-thin.ttf'
    path_to_font = str(path_to_font)
    font_size = 400
    font = ImageFont.truetype(path_to_font, font_size)
    text_box = draw.textbbox((0, 0), letter, font=font)
    x = (image.width - text_box[2]) / 2
    y = (image.height - text_box[3] - 80) / 2
    draw.text((x, y), letter, font=font, fill='white')
    image.save(input_image)
    return image


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile/Image')
    confidentiality = models.BooleanField(default=True, verbose_name='Confidentiality')
    url_website = models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to website')
    url_instagram = models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to instagram')
    url_telegram = models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to telegram')
    url_github = models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to github')
    likes = models.ManyToManyField('self', symmetrical=False, blank=True, verbose_name='Likes',
                                   related_name='liked_profiles')
    follow = models.ManyToManyField('self', blank=True, verbose_name='Followers',)
    
    def save(self, *args, **kwargs):
        if not self.image:
            default_image = generate_random_image(name_image=self.user.username)
            image = add_word_to_image(input_image=default_image, letter=self.user.username[0].upper())

            image_io = BytesIO()
            image.save(image_io, format='JPEG', quality=100)
            image_io.seek(0)
            self.image.save(f'{self.user.username}.JPEG', ContentFile(image_io.read()), save=False)

            if os.path.abspath(default_image):
                os.remove(default_image)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            image_path = path_image / f'{self.user.username}.JPEG'
            if os.path.exists(image_path):
                print(f'Delette image {image_path}')
                os.remove(image_path)

        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.user} Profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def total_likes(self):
        return self.likes.count()

    def followers(self):
        return self.follow.count()
    
        
class StarModel(models.Model):
    user_acc = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='User_account')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='User_added')
    star_num = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
