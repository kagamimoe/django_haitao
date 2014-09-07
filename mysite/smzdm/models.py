from django.db import models
from django.contrib import admin

# Create your models here.
class GoodsPost(models.Model):
	title = models.TextField()
	link = models.CharField(max_length = 150)
	pub_date = models.DateTimeField('date published')

	class Meta:
		ordering = ['-pub_date']

admin.site.register(GoodsPost)