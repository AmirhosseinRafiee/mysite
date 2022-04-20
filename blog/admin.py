from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
  date_hierarchy = 'created_date'
  empty_value_display = '-empty-'
  # fields = ('title', 'content', 'status', 'published_date') 
  exclude = ('counted_view',)
  list_display = ('title', 'author', 'status', 'counted_view', 'created_date', 'published_date')
  # ordeing = '-created_date'
  list_filter = ('status', 'author')
  search_fields = ('title', 'content')
  summernote_fields = ('content',)
  
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
