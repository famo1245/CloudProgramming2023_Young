from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment

admin.site.register(Post, MarkdownxModelAdmin) # admin에 post를 관리하는 사이트를 추가
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
