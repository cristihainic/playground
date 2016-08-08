from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import timezone
from .forms import PageForm, CommentForm
import datetime

from .models import Page, Comments

class PageListView(ListView):
    model = Page
    template_name = "page_list.html"

    def get_context_data(self):
        context = super(PageListView, self).get_context_data()
        context['this_year'] = datetime.date.today().year
        return context


def page(request, page_id):
    page_obj = Page.objects.get(pk=page_id)
    form_obj = CommentForm()
    comments = Comments.objects.filter(page=page_obj)
    if request.method == 'POST':
        data = request.POST.copy()
        data['page'] = page_id
        form_obj = CommentForm(data)
        if form_obj.is_valid():
            form_obj.instance.page_id = page_id
            #import ipdb; ipdb.set_trace()
            form_obj.save()
    return render_to_response(
        "page.html",
        context={'page': page_obj, 'this_year': datetime.date.today().year, 'comment_form': form_obj, 'comments': comments,},
        context_instance=RequestContext(request)
    )

def edit_post(request, page_id):
    page_obj = Page.objects.get(pk=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page_obj)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return HttpResponseRedirect(reverse("page_detail", kwargs={"page_id": page_obj.id}))
    else:
        form = PageForm(instance=page_obj)
    context={"form": form, "page_obj": page_obj}
    return render_to_response("page_edit.html", context, context_instance=RequestContext(request))
    #ultimul parametru e pentru csrf_token

def new_post(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.date_added = timezone.now()
            obj.save()
            return redirect('home')
    else:
        form = PageForm()
    return render(request, 'new.html', {'form': form})

def del_post(request, page_id):
    page_obj = Page.objects.get(pk=page_id)
    page_obj.delete()
    return redirect('home')
