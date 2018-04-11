from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='Title', max_length=250)
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(verbose_name='Updated Date', auto_now=True, editable=False)
    categories = models.ManyToManyField(verbose_name='Category', to='categories.Category', related_name='blogs')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return '{title}'.format(title=self.title)