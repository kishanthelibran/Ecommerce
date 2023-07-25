from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def RegisterUser(request):
    phone_number = request.data['phone_number']
    check_valid_number = User.objects.filter(phone_number=phone_number).first()
    if not check_valid_number:
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('User Registered')
    else:
        return Response('Phone Number Already Exists')
