from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render

from .models import *
from .serializers import CompanySeriallizer
from permissoin.models import Permission
from user.helper import get_user

class CompanyView(APIView):
    def get(self, request):
        
        try:
            companies = Company.objects.all()
            serializer = CompanySeriallizer(companies, many=True)
            return Response({"MESSAGE":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "your Target doesn't exist"},
                             status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.add_company and permission.add_list_item:
            try:
                company= MainCompany.objects.get(id=request.data.get('company'))
                companies = Company.objects.create(
                    name= request.data.get('name'),
                    commission= request.data.get('commission'),
                    bill_insurance = request.data.get('bill_insurance'),
                    commission_intermediary = request.data.get('commission_intermediary'),
                    company =company
                )
                companies.save()
                return Response({"MESSAGE":"Company created"}, 
                                status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response({"message": "your Target doesn't exist"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "you don't have permission"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.update_company:
            try:
                company = Company.objects.get(id=id)
                serializers = CompanySeriallizer(company, data=request.data, 
                                                partial=True)
                if serializers.is_valid():
                    serializers.save()
                    return Response({"MESSAGE":"Company updated"},
                                    status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"message": "your Target doesn't exist"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "you don't have permission"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.delete_company:
            try:
                company = Company.objects.get(id=id)
                company.delete()
                return Response({"MESSAGE":"Company deleted"},
                                status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"message": "your Target doesn't exist"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "you don't have permission"},
                            status=status.HTTP_400_BAD_REQUEST)
    
