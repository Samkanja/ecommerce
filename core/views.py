from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from item.models import Category,Item


class ItemListView(ListView):
    model = Item
    template_name = 'core/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return self.model.objects.filter(is_sold=False)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        return context




