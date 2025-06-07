from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from user.models import User
from .models import Permission, Group
from .serializers import PermissionSerializer, GroupSerializer
from user.helper import get_user
from company.models import MainCompany

class PermissionView(APIView):
    def get(self, request):
        try:
            permission = Permission.objects.all()
            ser = PermissionSerializer(permission, many=True)
            return Response({"data":ser.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Mesaage": "ERROR"},
                            status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, id):
        token = request.data.get('token')
        users = get_user(token)
        permission = Permission.objects.get(user=users)
        if permission.update_list or permission.update_item:
            try:
                # token = request.data.get('token')
                user = User.objects.get(id=id)
                print(user.username)
                permission = Permission.objects.get(user=user)
                ser = PermissionSerializer(permission, data=request.data, partial=True)
                if ser.is_valid():
                    ser.save()
                    permission.user = user
                    permission.save()
                    return Response({"data":ser.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"Mesaage": "ERROR"},
                                    status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response({"Mesaage": "ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"you don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)

class GroupView(APIView):
    def get(self, request, id):
        try:
            group = Group.objects.filter(company=id)
            ser = GroupSerializer(group, many=True)
            return Response({"data":ser.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Mesaage": "ERROR"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        # print(type(request.data.get('company')))
        if permission.add_list_item:
            try:
                company = MainCompany.objects.get(id=request.data.get('company'))
                group = Group.objects.create(name=request.data.get('name'),
                                             company=company)
                                             
                group.save()
                return Response({"data":"OK"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Mesaage": "ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"you don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)

    def put(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.update_list or permission.update_item:
            try:
                group = Group.objects.get(id=id)
                ser = GroupSerializer(group, data=request.data, partial=True)
                if ser.is_valid():
                    ser.save()
                    return Response({"data":ser.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"Mesaage": "ERROR"},
                                    status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response({"Mesaage": "ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"you don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, id):
        token = request.data.get("token")
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.delete_item or permission.delete_list:
            try:
                group = Group.objects.get(id=id)
                group.delete()
                return Response({"data":"OK"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Mesaage": "ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"you don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)

        
            