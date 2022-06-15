import email
import imp
from lib2to3.pgen2 import token
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, MemberSerializer
from .models import Memberuserdata as User
from .models import Memberdata as Member
from .models import Whitelistdata as WL
from .models import Whitelistrecdata as WLR
from django.db.models import Q
from django.db import connection
import jwt, datetime
from django.http import JsonResponse
import json

cursor = connection.cursor()
    
# Create your views here.
class AutoCompFruitsView(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')            
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id, user.group_imwy, user.region)
        try:
            if user.group_imwy == 'Center Dept':
                if int(user.internal_position) > 3:
                    cursor.execute('EXEC spAutoComp_CM %s',(user.id, ))
                else:
                    cursor.execute('EXEC spAutoComp_CT %s, %s, %s',(user.id, user.group_imwy, user.region))
            else:
                if int(user.internal_position) > 2:
                    cursor.execute('EXEC spAutoComp_CM %s',(user.id, ))
                else:
                    cursor.execute('EXEC spAutoComp_EV %s, %s',(user.id, user.membergroup))   
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]
            results = json.dumps(results)
        finally:
            cursor.close()
        response = Response()
        response.data = {'fruits': results}
        return response
    
# Create your views here.
class CheckDFView(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')   
               
        platform = request.data['platform']
        userName = request.data['userName']   
        mobile = request.data['mobile']   
        print(platform,userName,mobile)
        print(token)
        print(jwt.decode(token, 'secret', algorithms=['HS256']))
        if not token:
            raise AuthenticationFailed('Unauthorized!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')            
        user = Member.objects.filter(id = payload['id']).first()
        try:
            body = [platform, userName, mobile]
            print(body)
            cursor.execute('EXEC spCheckDF %s, %s, %s, %s',(user.uid, userName, platform, mobile))
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]
            # results = json.dumps(results)
        finally:
            print(results)
        response = Response()
        response.data = {'result': results}
        return response