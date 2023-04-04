from django.contrib import admin
from .models import Post, Category

admin.site.register(Post) # admin에 post를 관리하는 사이트를 추가


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
