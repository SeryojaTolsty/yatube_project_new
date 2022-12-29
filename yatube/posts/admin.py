from django.contrib import admin

# Register your models here.

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисление полей, отображаемых в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Добавление интерфейса для поиска постов по тексту
    list_editable = ('group',)
    search_fields = ('text',)
    # Добавление возможности фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
