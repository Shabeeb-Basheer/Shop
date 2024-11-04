from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =  ("name", "phone")
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)

@admin.register(Product)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)

admin.site.register(CustomerFeedback)
admin.site.register(Client)
@admin.register(ProductEnquiry)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ("name", "phone","product","email")

# admin.site.register(UpdateStatus)