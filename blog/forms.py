from .models import CommentModel, PostModel
from django import forms


class AddCommentFormUsername(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('username' ,'comment',)
        
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'id_query', 'class': 'form-control'}))


class AddPost(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'category', 'image1', 'content1', 'image2', 'content2', 
                  'image3', 'content3', 'image4', 'content4', 'image5', 'content5', 'image6', 'content6', 
                  'image7', 'content7', 'image8', 'content8', 'image9', 'content9', 'image10', 'content10', 'image11', 'content11' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'content1': forms.Textarea(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'content2': forms.Textarea(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
            'content3': forms.Textarea(attrs={'class': 'form-control'}),
            'image4': forms.FileInput(attrs={'class': 'form-control'}),
            'content4': forms.Textarea(attrs={'class': 'form-control'}),
            'image5': forms.FileInput(attrs={'class': 'form-control'}),
            'content5': forms.Textarea(attrs={'class': 'form-control'}),
            'image6': forms.FileInput(attrs={'class': 'form-control'}),
            'content6': forms.Textarea(attrs={'class': 'form-control'}),
            'image7': forms.FileInput(attrs={'class': 'form-control'}),
            'content7': forms.Textarea(attrs={'class': 'form-control'}),
            'image8': forms.FileInput(attrs={'class': 'form-control'}),
            'content8': forms.Textarea(attrs={'class': 'form-control'}),
            'image9': forms.FileInput(attrs={'class': 'form-control'}),
            'content9': forms.Textarea(attrs={'class': 'form-control'}),
            'image10': forms.FileInput(attrs={'class': 'form-control'}),
            'content10': forms.Textarea(attrs={'class': 'form-control'}),
            'image11': forms.FileInput(attrs={'class': 'form-control'}),
            'content11': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
