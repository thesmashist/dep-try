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
    
# Create your views here.
class AutoCompFruitsView(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')
        cursor = connection.cursor()
        
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
                    cursor.execute('EXEC spAutoComp_CM %s',(user.uid, ))
                else:
                    cursor.execute('EXEC spAutoComp_CT %s, %s, %s',(user.id, user.group_imwy, user.region))
            else:
                if int(user.internal_position) > 2:
                    cursor.execute('EXEC spAutoComp_CM %s',(user.uid, ))
                else:
                    cursor.execute('EXEC spAutoComp_EV %s',(user.uid,))   
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]
            results = json.dumps(results)
        finally:
            cursor.close()
        response = Response()
        response.data = {'fruits': results}
        return response