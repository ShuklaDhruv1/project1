from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SpaceTopic

@admin.register(SpaceTopic)
class SpaceTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic_type')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('topic_type',)