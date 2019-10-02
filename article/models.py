import datetime
from django.db import models
from django.utils import timezone
from category.models import Category

class Article(models.Model):
    category_id = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    user_id = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def category(self):
        c = Category.objects.get(pk=self.category_id)
        return c.name;
