from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import timezone
from .forms import PageForm

from .models import Page

class PageListView(ListView):
    model = Page
    template_name = "page_list.html"

def index(request):
    return HttpResponse("Hello Word!")

def page(request, page_id):
    page_obj = Page.objects.get(pk=page_id)
    return render_to_response(
        "page.html",
        context={'page': page_obj},
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
