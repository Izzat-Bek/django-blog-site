from .models import Category
from random import randint


def category(request):
    return {'category': Category.objects.all().order_by('name')}


def user_identificator(request):
    if request.user.is_authenticated:
        return {'user_identifier': request.user.username}
    else:
        user_iden = request.session.get('user_identifier')
        if not user_iden:
            user_iden = f'User-{randint(100000000, 1000000000)}'
            request.session['user_identifier'] = user_iden
        return {'user_identifier': user_iden}




