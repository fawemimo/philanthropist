from django.contrib import admin
from .models import *
from django.utils.html import format_html, urlencode

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone', 'message')
    list_display_links = ('name', 'email')


@admin.register(Philanthropist)
class PhilanthropistAdmin(admin.ModelAdmin):
    list_display = ('name','profile_pix','date_of_birth')

    def profile_pix(self, instance):
        if instance.display_pics.name != "":
            return format_html(
                f'<img src="{instance.display_pics.url}" class="thumbnail"/>'
            )
        return "No Profile Pics Added"

    class Media:
        css = {"all": ["css/styles.css"]}


@admin.register(ReadOurNew)
class ReadOurNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('name','position','display_picture')

    def display_picture(self, instance):
        if instance.display_pic.name != "":
            return format_html(
                f'<img src="{instance.display_pic.url}" class="thumbnail"/>'
            )
        return "No Profile Pics Added"

    class Media:
        css = {"all": ["css/styles.css"]}

