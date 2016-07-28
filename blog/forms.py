from django.forms.models import ModelForm
from blog.models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ['date_added',]

