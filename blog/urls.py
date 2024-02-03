from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.post_detail, name='details')
]