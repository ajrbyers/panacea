from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Journal(models.Model):
	name = models.CharField(max_length=30, help_text='The name of this journal')
	logo = models.ImageField(null=True)


class Article(models.Model):
	title = models.CharField(max_length=255)
	subtitle = models.CharField(max_length=255)
	abstract = models.TextField(null=True)

	date_submitted = models.DateTimeField(default=timezone.now)
	date_published = models.DateTimeField(null=True)

	owner = models.ForeignKey(User, related_name='owner')
	authors = models.ManyToManyField(User, related_name='authors')

	open_for_comments = models.BooleanField(default=True)
	doi = models.CharField(max_length=255, null=True)
	license = models.ForeignKey('License')

	manuscript_file = models.FileField(null=True)


class Version(models.Model):
	article = models.ForeignKey(Article)
	html = models.TextField()
	number = models.PositiveIntegerField(default=0)
	draft = models.BooleanField(default=True)
	date_published = models.DateTimeField(null=True)

	class Meta:
		ordering = ('number',)


class License(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True)
	url = models.URLField(null=True)

	def __str__(self):
		return self.name