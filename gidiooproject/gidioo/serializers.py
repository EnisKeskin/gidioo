from .models import Entry,Category,Tag,EntryTag,Repeat
from rest_framework import serializers


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('id','category','date','amount','income_expense')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class RepeaterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repeat
        fields = ('repeat','entry','date')

class EntryTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntryTag
        fields = ('__all__') 

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url','id','name',)

class InAndExSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('id','category','date','amount','income_expense')