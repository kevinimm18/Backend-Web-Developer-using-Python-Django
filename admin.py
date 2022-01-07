from django.contrib import admin

# Register your models here.

from .models import contact, Content_List

class contactAdmin(admin.ModelAdmin):
    list_display =['id', 'Email', 'Subject']

admin.site.register(contact, contactAdmin)

class Content_ListAdmin(admin.ModelAdmin):
    readonly_fields=[
        'slug',
        'Updated',
        'Published'
    ]

    list_display =['id', 'Judul', 'Kategori']

admin.site.register(Content_List, Content_ListAdmin)