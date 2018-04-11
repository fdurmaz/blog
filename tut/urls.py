from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from blogs.views import IndexView, DetailView

urlpatterns = [
    path('detail/<int:blog_id>/', DetailView.as_view(), name='detail'),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
