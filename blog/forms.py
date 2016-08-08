from django.forms.models import ModelForm
from blog.models import Page, Comments


class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ['date_added',]

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        exclude=['page',]

