from django.contrib import admin
from django.urls import path

from blogs.views import IndexView, DetailView, FilterView

urlpatterns = [
    path('detail/<int:blog_id>/', DetailView.as_view(), name='detail'),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
