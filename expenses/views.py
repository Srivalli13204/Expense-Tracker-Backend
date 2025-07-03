from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.views import APIView
from django.db.models import Sum

# Create your views here.
class ExpenseCreateView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        start = self.request.query_params.get('start_date')
        end = self.request.query_params.get('end_date')
        if start and end:
            return Expense.objects.filter(user=user, date__range=[start, end])
        return Expense.objects.filter(user=user)
    
class ExpenseAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        total = expenses.aggregate(total=Sum('amount'))['total'] or 0
        category_breakdown = expenses.values('category').annotate(total=Sum('amount'))
        return Response({
            'total_expenses' : total,
            'category_breakdown' : category_breakdown,
        })