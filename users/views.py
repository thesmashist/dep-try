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

    
wlTitles = ['CSAM','All']; 
csamList = []; 
allList = []; 

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        print(username)
        print(password)
        wlid = []
        
        user = User.objects.filter(username=username).first()
        print(user)
        wl = WL.objects.filter(wid__in=WLR.objects.filter(memberid=user.uid))
        print(wl)
        for i in wl:
            wlid.append(i.title)
        member = Member.objects.filter(id = user.id).first()
        print(member.internal_position)
        if member.internal_position == 1 or (member.membergroup == 'Department' and member.tgw and member.condition == 'Active') or 'All' in wlid:
            wlid.append('Leader')
        if int(member.internal_position) < 3 or 'All' in wlid:
            wlid.append('EVLeader')
        if member.bbt or 'All' in wlid:
            wlid.append('BBT')
        serializer = MemberSerializer(member)     
        
        if user is None:
            raise AuthenticationFailed('User not found!')

        if user.password != password:
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=(60*24)),
            'iat': datetime.datetime.utcnow(),
            'user': serializer.data,
            'roles': wlid
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='token',value=token, httponly=True)
        response.data = {'token': token}
        return response
    
# Create your views here.
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        
        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')            
        user = Member.objects.filter(id = payload['id']).first()
        serializer = MemberSerializer(user)
        return Response(serializer.data)
    
# Create your views here.
class AutoCompMemberView(APIView):
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
        try:
            cursor.execute('EXEC spAutoCompM %s',(user.region,)) 
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]
            results = json.dumps(results)
        finally:
            cursor.close()
        response = Response()
        response.data = {'leaves': results}
        return response
    
# Create your views here.
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {'message':'Success'}
        
        return response

    
# Create your views here.
class GEVAInitView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        memCursor = connection.cursor()
        seasonCursor = connection.cursor()
        
        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')            
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id)
        try:
            memCursor.execute('EXEC spGevaGetMember %s',(user.uid,)) 
            members = [ dict( zip( [column[0] for column in memCursor.description] , record ) ) for record in memCursor.fetchall()]
            # members = json.dumps(members)
            seasonCursor.execute('EXEC spGetEVSeasonPerRegion %s',(user.region,)) 
            season = seasonCursor.fetchall()
            result = {
                'Season': season,
                'Members': members
            }
        finally:
            memCursor.close()
            seasonCursor.close()
        
        return Response(result)
    
# Create your views here.
class BBTAPInitView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        seasonCursor = connection.cursor()
        regionCursor = connection.cursor()
        
        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')            
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id)
        try:
            regionCursor.execute('SELECT Region, Position P FROM RegionData') 
            regions = [ dict( zip( [column[0] for column in regionCursor.description] , record ) ) for record in regionCursor.fetchall()]
            seasonCursor.execute('SELECT * FROM EVSeason WHERE Region != %s ORDER BY ID DESC',('Test',)) 
            seasons = [ dict( zip( [column[0] for column in seasonCursor.description] , record ) ) for record in seasonCursor.fetchall()]
            result = {
                'Seasons': seasons,
                'Regions': regions,
                'MyRegion': user.region
            }
        finally:
            regionCursor.close()
            seasonCursor.close()
        
        return Response(result)    
  