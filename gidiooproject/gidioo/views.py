from .models import Entry,Category,Repeat,Tag,EntryTag
from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import EntrySerializer, CategorySerializer, RepeaterSerializer, TagSerializer, EntryTagSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (IsAuthenticated,) 
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['id']
    def get_queryset(self):
        query = self.request.query_params.get('id', None)
        if query is not None:
            print(query)
            return Entry.objects.filter(id = query)
        return Entry.objects.all()
    
    @action(methods=['get'],detail=True)
    def statistics(self, request, pk=None):
        entry = Entry.objects.all()
        income = 0
        expense = 0
        for e in entry:
            if e.income_expense == True:
             income += e.amount
            else:
             expense+= e.amount
        all_amount = income-expense
        serializer_context = {
            'request': request,
        }
        serializer = EntrySerializer(many=True, context=serializer_context)
        return Response({'income-sum': income if income else 0,'expense-sum': expense if expense else 0 , 'statistics': all_amount if all_amount else 0,'objects': serializer.data})
        
    @action(methods=['get'],detail=True)
    def category(self, request, pk=None):
        entry = Entry.objects.all().values('category').annotate(total=Count('category'))
        serializer_context = {
            'request': request,
        }
        serializer = EntrySerializer(many=True, context=serializer_context)
        return Response({'entry': entry if entry else 0,})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,) 
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    def get_queryset(self):
        query = self.request.query_params.get('name', None)
        if query is not None:
            return Category.objects.filter(name = query)
        return self.queryset

class RepeaterViewSet(viewsets.ModelViewSet):
    queryset = Repeat.objects.all()
    serializer_class = RepeaterSerializer
    permission_classes = (IsAuthenticated,) 

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,) 

class EntryTagViewSet(viewsets.ModelViewSet):
    queryset = EntryTag.objects.all()
    serializer_class = EntryTagSerializer
    permission_classes = (IsAuthenticated,) 
