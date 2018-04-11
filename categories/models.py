from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=250)
    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(verbose_name='Updated Date', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{title}'.format(title=self.title)
