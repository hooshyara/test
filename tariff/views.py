from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from .models import *
from .serializers import *
from booking.models import Sailing
from booking.serializers import SailingSerializer
from user.helper import get_user
from permissoin.models import Permission

class TariffView(APIView):
    def get(self, request):
        try:
            sailing = Sailing.objects.all()
            sailing_serializer = SailingSerializer(sailing, many=True)
            tariffs = Tariff.objects.all()
            serializer = TariffSerializers(tariffs, many=True)
            return Response({"data":serializer.data,
                            "Sailing":sailing_serializer.data}
                            , status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Message":"your Target doesn't exist"},
                            status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.add_demurrage:
        # if 2 > 1:
            try:
                sailing = Sailing.objects.get(id=request.data.get('sailing'))
                payment_method = Sailing.objects.get(id=request.data.get('sailing'))
                tariff = Tariff.objects.create(
                    sailing=sailing,
                    payment_method=payment_method,
                    from_day = request.data.get('from_day'),
                    until_day = request.data.get('until_day'),
                    foot = request.data.get('foot'),
                    sailing_price = request.data.get('sailing_price'),
                    company =None
                )
                tariff.save()
                return Response({"Message":"OK"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Message":"ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.update_demurrage:
        # if 2 > 1:
            try:
                tariff = Tariff.objects.get(id=id)
                tariff_serializers = TariffSerializers(tariff, data=request.data,
                                                    partial=True)
                if tariff_serializers.is_valid():
                    tariff_serializers.save()
                    return Response({"Message":"OK"}, status=status.HTTP_200_OK)
                else:
                    print(tariff_serializers.errors)
                    return Response({"Message":"Target Dosn't Exist"},
                                    status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response({"Message":"ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.delete_demurrage:
        # if 2 > 1:
            try:
                tariff = Tariff.objects.get(id=id)
                tariff.delete()
                return Response({"Message":"OK"}, status=status.HTTP_200_OK)
            except Exception as e :
                print(e)
                return Response({"Message":"Target Dosn't Exist"},
                                    status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
class WarehousingTariffView(APIView):
    def get(self, request):
        try:
            warehousing_tariff = WarehousingTariff.objects.all()
            tariff_serializers = WarehousingTariffSerializers(warehousing_tariff, many=True)
            return Response({"data":tariff_serializers.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Message":"ERROR"},
                            status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.add_warehousing:
            try:
                warehousing_tariff = WarehousingTariff.objects.create(
                    max_days = request.data.get('max_days'),
                    foot = request.data.get('foot'),
                    price = request.data.get('price'),
                    company =None
                )
                warehousing_tariff.save()
                return Response({"Message":"OK"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Message":"ERROR"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
    def put(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.update_warehousing:
            try:
                warehousing_tariff = WarehousingTariff.objects.get(id=id)
                warehousing_tariff_serializers = WarehousingTariffSerializers(warehousing_tariff,  data=request.data,
                                            partial=True)
                if warehousing_tariff_serializers.is_valid():
                    warehousing_tariff_serializers.save()
                    return Response({"Message":"OK"}, status=status.HTTP_200_OK)
                else:
                    print(warehousing_tariff_serializers.errors)
                    return Response({"Message":"Target Dosn't Exist"},
                                    status=status.HTTP_404_NOT_FOUND)
            except Exception as e : 
                print(e)
                return Response({"Message":"Target Dosn't Exits"})
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, id):
        token = request.data.get('token')
        user = get_user(token)
        permission = Permission.objects.get(user=user)
        if permission.delete_warehousing:
            try:
                warehousing_tariff = WarehousingTariff.objects.get(id=id)
                warehousing_tariff.delete()
                return Response({"Message":"OK"}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Message":"Target Doesn't Exist"},
                                    status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Message":"You don't have permission"},
                            status=status.HTTP_403_FORBIDDEN)

