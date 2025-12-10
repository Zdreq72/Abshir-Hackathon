from django.contrib import admin
from .models import Cluster

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'confidence', 'source', 'created_at')
    list_filter = ('source', 'confidence')
    search_fields = ('title',)