# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :


from django.db import models
import calendar

# Create your models here.


class Category(models.Model):
	title = models.CharField(max_length=100, primary_key = True)
	slug = models.SlugField(max_length=100, db_index=True)
	
	def __unicode__ (self):
		return str(self.title)

class Entry(models.Model):
	ID = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted  = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey(Category)

	def __unicode__ (self):
		return str(self.title)


	@models.permalink
	def get_absolute_url(self):
		return('view_blog_post', None, {'slug': self.slug})

class Author(models.Model):
	surname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	
	
	def __unicode__ (self):
		return str(self.lastname)

	class Meta:
		ordering = ('lastname',)

class Book(models.Model):
	title = models.TextField()
	author = models.ManyToManyField(Author)
	
	
	def __unicode__ (self):
		return str(self.title)


class Citation(models.Model):
	body = models.TextField()
	author = models.ForeignKey(Author)
	book = models.ForeignKey(Book)
	
	def __unicode__ (self):
		return str(self.title)



