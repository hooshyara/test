from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth.hashers import check_password, make_password
from .models import User
from .serializers import UserSeriallizer
# import socket
# from django.core.mail import send_mail
# from django.dispatch import receiver
# from django.core.signals import request_started
# from .signal import send_email
from .helper import get_user
from permissoin.models import Permission
from booking.models import Truck
from booking.serializers import TruckSerializers
from company.models import MainCompany
class UserView(APIView):

    def get(self, request, id):
        try:
            user = User.objects.filter(company=id)
            serializers = UserSeriallizer(user, many=True)
            return Response({"users": 
                             serializers.data}, status=status.HTTP_200_OK)
        except:
            return Response({"message": 
                             "User doesn't exist "}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        token = request.data.get("token")
        users = get_user(token)
        permissions = Permission.objects.get(user=users)
        if permissions.add_list_item:
            try:
                company = MainCompany.objects.get(id=request.data.get('company'))
                username = request.data.get('username')
                fullName  = request.data.get('fullName')
                phone = request.data.get('phone')
                password = request.data.get('password')
                personal_code = request.data.get('personal_code')
                Hashed_password = make_password(password)

                user = User.objects.create(
                    username=username,
                    phone=phone,
                    password=Hashed_password,
                    fullName=fullName,
                    personal_code=personal_code,
                    company =company
                )
                user.save()
                permission = Permission.objects.create(
                    user=user,
                    access=False,
                    add_list_item=False,
                    update_list=False,
                    delete_list=False,
                    delete_item=False,
                    update_item=False,
                    add_owner_of_goods=False,
                    delete_owner_of_goods=False,
                    update_owner_of_goods=False,
                    add_rout=False,
                    update_rout=False,
                    delete_rout=False,
                    add_station=False,
                    update_station=False,
                    delete_station=False,
                    add_truck=False,
                    update_truck=False,
                    delete_truck=False,
                    add_driver=False,
                    update_driver=False,
                    delete_driver=False,
                    add_company=False,
                    update_company=False,
                    delete_company=False,
                    add_demurrage=False,
                    update_demurrage=False,
                    delete_demurrage=False,
                    add_warehousing=False,
                    update_warehousing=False,
                    delete_warehousing=False,
                    users=False,
                    add_bill=False,
                    update_bill=False,
                    disable_bill=False,
                    add_continer=False,
                    update_continer=False,
                    delete_continer=False,
                    manage_attachments=False,
                    container_demurrage_management=False,
                    booking_management=False,
                    truck_exit=False,
                    management_of_loading_costs=False,
                    Upload_the_documents_attached_to_the_bill_of_lading=False,
                    list_of_issued_bills_of_lading=False
                )
                permission.save()
                return Response({"message": 
                                "User created successfuly"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"message": 
                                "ERROR"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":
                             "You don't have permission"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, id):
        token = request.data.get("token")
        users = get_user(token)
        permission = Permission.objects.get(user=users)
        if permission.update_list or permission.update_item:
            try:
                user = User.objects.get(id=id)
                print(user.id)
                serializes = UserSeriallizer(user, data=request.data, partial=True)
                if serializes.is_valid():
                    if serializes.validated_data['password']:
                        serializes.validated_data['password'] = make_password(serializes.validated_data['password'])
                    serializes.save()
                    print(serializes.data)
                    return Response({'message': 'User edited successfully'}, status=status.HTTP_200_OK)
                
                else:
                    print(serializes.errors)
                    return Response({"ERROR" : serializes.errors}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response({"message": 
                                "User doesn't exist "}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, id):
        token = request.data.get("token")
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.update_item or permission.update_list:
            try:
                user = User.objects.get(id=id)
                if user.is_superuser:
                    return Response({"message":"این کاربر قابل حذف شدن نمیباشد"})
                else:
                    user.delete()
                    return Response({'message': 'User Deleted successfully  '}, status=status.HTTP_200_OK)
            except:
                return Response({"message": 
                                "User doesn't exist "},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
class LoginView(APIView):
    
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.get(username=username)
            print(username)
            print(password)
            # send_server_ip()
            if OutstandingToken.objects.filter(user=user).exists():
                out = OutstandingToken.objects.get(user=user)
                # print(out)
                # out.delete()

                # tk = RefreshToken(out.token)
                # tk.blacklist()
                # print(out.token)

                OutstandingToken.objects.filter(user=user).delete()
                  

            if username and password:
                if user.check_password(password):
                    truck = Truck.objects.all()
                    truck_serializers = TruckSerializers(truck, many=True)
                    refresh_token = RefreshToken.for_user(user)
                    access_token = refresh_token.access_token
                    user_serializer = UserSeriallizer(user)
                    return Response({
                    'refresh_token': str(refresh_token),
                    'access_token': str(access_token),
                    'user': user_serializer.data,
                    "truck": truck_serializers.data
                }, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'Incorrect password'},
                                    status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"message": "error"},
                                status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({"message": "error"},
                             status=status.HTTP_400_BAD_REQUEST)
        


class CheckUser(APIView):
    def post(self, request):
        try:
            token = request.data.get('token')
            user = get_user(token)
            ser = UserSeriallizer(user, many=False)
            return Response({"user":ser.data})
            
        except Exception as e:
            print(e)
            return Response({"message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)
        
class LogOutView(APIView):
    def post(self, request):
        refresh_token= request.data.get('token')
        print(refresh_token)
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                out_token = OutstandingToken.objects.get(token= token)
                BlacklistedToken.objects.create(token= out_token)
                out_token.delete()
                return Response({'message': 'successfuly loged out'},
                                 status= status.HTTP_205_RESET_CONTENT)
            except TokenError:
                return Response({'error': 'Invalid refresh token'},
                                status= status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'please provide a refresh token'},
                         status= status.HTTP_400_BAD_REQUEST)
        

