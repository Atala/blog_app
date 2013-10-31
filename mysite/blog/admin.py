from django.contrib import admin
from models import *


class EntryAdmin(admin.ModelAdmin) :
	title = "title"
	slug = title.replace(' ', '_')
	prepopulated_fields = {"slug": (slug,)}
	

class CategoryAdmin(admin.ModelAdmin) :
	title = "title"
	slug = title.replace(' ', '_')
	prepopulated_fields = {"slug": (slug,)}
	

class CitationAdmin(admin.ModelAdmin) :
	pass

class AuthorAdmin(admin.ModelAdmin) :
	pass

class BookAdmin(admin.ModelAdmin) :
	pass

class BookAdmin(admin.ModelAdmin) :
	pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Citation, CitationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
