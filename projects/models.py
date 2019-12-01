from django.db import models

# Create your models here.
# model is called projects and it will contain the
# fields- title, description, technology and image.
#so create a class
# Django models come with many built in model field types.
# By default django creates databases in sqlite 
# but mysql postgresql can also be used as a sql language with the django orm


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length = 20)
	image = models.FilePathField(path="/img")

