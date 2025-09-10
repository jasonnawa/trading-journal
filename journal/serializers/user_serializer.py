from django.contrib.auth.models import User
from journal.models import JournalEntry
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    journal = serializers.PrimaryKeyRelatedField(many=True, queryset=JournalEntry.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'username','is_staff',  'email', 'journal']