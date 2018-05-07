from django.shortcuts import redirect
from django.views.generic import TemplateView

from blogs.models import Blog
from categories.models import Category


class IndexView(TemplateView):
    template_name = 'blogs/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        category = self.request.GET.get('category', None)

        if category:
            blogs = Blog.objects.filter(categories=category)
        else:
            blogs = Blog.objects.all().order_by('-created_date')
        categories = Category.objects.all()

        context.update({
            'title': 'Blog',
            'blogs': blogs,
            'categories': categories
        })
        return context


class DetailView(TemplateView):
    template_name = 'blogs/detail.html'

    def dispatch(self, request, blog_id, *args, **kwargs):
        try:
            self.blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            self.blog = None
            return redirect('index')

        return super(DetailView, self).dispatch(request, blog_id, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        context.update({
            'title': 'Blog Detail',
            'blog': self.blog,
            'categories': self.blog.categories.all()
        })
        return context


class FilterView(TemplateView):
    template_name = 'blogs/filter.html'
