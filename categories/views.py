from django.views.generic import TemplateView

from .models import Category


class IndexView(TemplateView):
    template_name = 'blogs/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context.update({
            'title': 'Category',
            'domain_admin_panel': '/admin/',
            'categories': categories,
        })
        return context
