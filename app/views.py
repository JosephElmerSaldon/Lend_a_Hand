from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, User
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'
    
class BasePageView(TemplateView):
    template_name = 'app/base.html'

class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'app/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'app/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description', 'owner', 'is_available']
    template_name = 'app/item_create.html'
    context_object_name = 'owners'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description', 'owner', 'is_available']
    template_name = 'app/item_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'app/item_delete.html'
    success_url = reverse_lazy('item')