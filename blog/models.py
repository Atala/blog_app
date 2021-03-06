# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :


from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__ (self):
        return self.title


class Author(models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
 
    def __unicode__ (self):
        return self.lastname

    class Meta:
        ordering = ('lastname',)


def gen_save_path(instance, filename):
     """Generates the path as a string for fileStack field."""
     return 'images/' + instance.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ManyToManyField(Author, related_name = 'author')
    translator = models.ManyToManyField(Author, related_name = 'translator', blank = True, null = True)
    language = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="images", blank = True, null = True)
    
    def __unicode__ (self):
        return self.title


class Entry(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted  = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category)
    book = models.ForeignKey(Book, blank = True, null = True)

    def __unicode__ (self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return('view_blog_post', None, {'slug': self.slug})


class Citation(models.Model):
    body = models.TextField()
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book, blank = True, null = True)
    
    def __unicode__(self):
	srt = self.body[:15]
	srt += '...'
	return srt     




