from django.urls import path
from django.views.generic.base import RedirectView

from . import views as v

app_name ='core'

urlpatterns = [
    # path('',v.ProductView.as_view(),name='ProductView'),
    path('',v.LearnTemplateView.as_view(),name='LearnTemplateView'),
    # path('redirectview',RedirectView.as_view(url='http://www.swynfords.com/'),name='redirectview'),
    path('PreLoadTask/<int:pk>',v.PreLoadTask.as_view(),name='PreLoadTask'),
    path('SinglePost/<int:pk>',v.SinglePost.as_view(),name='SinglePost'),

]
