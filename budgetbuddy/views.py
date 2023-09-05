from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Transaction, Budget, Income, UserTotal
from .serializers import TransactionSerializer, BudgetSerializer, IncomeSerializer, UserTotalSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

class UserTotalViewSet(viewsets.ModelViewSet):
    queryset = UserTotal.objects.all()
    serializer_class = UserTotalSerializer
     # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    @action(detail=True, methods=['get', 'put', 'delete'])
    def user_incomes(self, request, pk=None):
        if request.method == 'GET':
            user_incomes = Income.objects.filter(user_id=pk)
            serializer = IncomeSerializer(user_incomes, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            user_incomes = Income.objects.filter(user_id=pk)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = IncomeSerializer(user_incomes, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user_incomes = Income.objects.filter(user_id=pk)
            user_incomes.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get', 'put', 'delete'])
    def user_entries(self, request):
        if request.method == 'GET':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Income.objects.filter(user_id=user)
            serializer = IncomeSerializer(user_entries, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Income.objects.filter(user_id=user)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = IncomeSerializer(user_entries, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Income.objects.filter(user_id=user)
            user_entries.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['delete'])
    def delete_last_entry(self, request):
        username = request.query_params.get('username')
        user = get_object_or_404(User, username=username)
        user_entries = Income.objects.filter(user_id=user).order_by('-id')
        
        if user_entries.exists():
            last_entry = user_entries.first()
            last_entry.delete()
            return Response({'detail': 'Last entry deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'No Income entries for the user.'}, status=status.HTTP_404_NOT_FOUND)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    @action(detail=True, methods=['get', 'put', 'delete'])
    def user_incomes(self, request, pk=None):
        if request.method == 'GET':
            user_incomes = Transaction.objects.filter(user_id=pk)
            serializer = TransactionSerializer(user_incomes, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            user_incomes = Transaction.objects.filter(user_id=pk)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = TransactionSerializer(user_incomes, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user_incomes = Transaction.objects.filter(user_id=pk)
            user_incomes.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get', 'put', 'delete'])
    def user_entries(self, request):
        if request.method == 'GET':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Transaction.objects.filter(user_id=user)
            serializer = TransactionSerializer(user_entries, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Transaction.objects.filter(user_id=user)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = TransactionSerializer(user_entries, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Transaction.objects.filter(user_id=user)
            user_entries.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['delete'])
    def delete_last_entry(self, request):
        username = request.query_params.get('username')
        user = get_object_or_404(User, username=username)
        user_entries = Transaction.objects.filter(user_id=user).order_by('-id')
        
        if user_entries.exists():
            last_entry = user_entries.first()
            last_entry.delete()
            return Response({'detail': 'Last entry deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'No Transaction entries for the user.'}, status=status.HTTP_404_NOT_FOUND)

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    # permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    @action(detail=True, methods=['get', 'put', 'delete'])
    def user_incomes(self, request, pk=None):
        if request.method == 'GET':
            user_incomes = Budget.objects.filter(user_id=pk)
            serializer = BudgetSerializer(user_incomes, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            user_incomes = Budget.objects.filter(user_id=pk)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = BudgetSerializer(user_incomes, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            user_incomes = Budget.objects.filter(user_id=pk)
            user_incomes.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get', 'put', 'delete'])
    def user_entries(self, request):
        if request.method == 'GET':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Budget.objects.filter(user_id=user)
            serializer = BudgetSerializer(user_entries, many=True)
            return Response(serializer.data)
        elif request.method == 'PUT':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Budget.objects.filter(user_id=user)
            updated_data = request.data  # Assuming you're sending updated data in the PUT request
            serializer = BudgetSerializer(user_entries, data=updated_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            username = request.query_params.get('username')
            user = get_object_or_404(User, username=username)
            user_entries = Budget.objects.filter(user_id=user)
            user_entries.delete()  # Delete the user's income entries
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['delete'])
    def delete_last_entry(self, request):
        username = request.query_params.get('username')
        user = get_object_or_404(User, username=username)
        user_entries = Budget.objects.filter(user_id=user).order_by('-id')
        
        if user_entries.exists():
            last_entry = user_entries.first()
            last_entry.delete()
            return Response({'detail': 'Last entry deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'No Budget entries for the user.'}, status=status.HTTP_404_NOT_FOUND)