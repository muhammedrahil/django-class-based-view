
from django.shortcuts import render,get_object_or_404
from django.views import View
from .form import ProductForm
from .models import Product
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.
from django.db.models import  F

class ProductView(View):
    form_class=ProductForm
    template_name='index.html'
    def get(self,request):
        form=self.form_class()
        context={
            'form':form
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
        context={
            'form':form
        }
        return render(request,self.template_name,context)


class LearnTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Product.objects.all()
        print(context)
        return context


class PreLoadTask(RedirectView):
    pattern_name = 'core:SinglePost'

    def get_redirect_url(self, *args, **kwargs):
        product= Product.objects.filter(pk=kwargs['pk'])
        product.update(price=F('price')+1)    
        return super().get_redirect_url(*args, **kwargs)


class SinglePost(TemplateView):
    template_name = 'redirect.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['data']=get_object_or_404(Product,pk=self.kwargs.get('pk'))
        return context