from django.urls import path

from blogs.views import IndexView

urlpatterns = [
    path('blogs/', IndexView.as_view()),
]
