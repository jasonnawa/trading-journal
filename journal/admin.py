from django.contrib import admin
from .models import JournalEntry, Strategy, Ticker, Tag

#TODO: Register with a ModelAdmin class (best practice for control)
admin.site.register(JournalEntry)
admin.site.register(Strategy)
admin.site.register(Ticker)
admin.site.register(Tag)