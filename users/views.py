import email
import imp
from lib2to3.pgen2 import token
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, MemberSerializer,MemberLoginDataSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Memberuserdata as User, Memberdata as Member, Whitelistdata as WL, Whitelistrecdata as WLR
from forms.models import Memberlogindata
from django.db.models import Q
from django.db import connection
import jwt, datetime
from django.utils import timezone
from django.utils.timezone import now
from django.http import JsonResponse

from rest_framework import generics, mixins
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend

from members import models, serializers
from members.models import Memberdata as Member
from members.serializers import MemberSerializer

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
        if member.internal_position == "1"or (member.membergroup == 'Department' and member.tgw and member.condition == 'Active') or 'All' in wlid:
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



class BBTList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
        queryset = Member.objects.filter(bbt = 1, btm__isnull=False).exclude(Q(region = "Perth"))
        serializer_class = MemberSerializer

        @method_decorator(cache_page(60*60*2))
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

class WhiteList():
    def getWhiteList():
        cursor = connection.cursor()
        query = cursor.execute("""
            SELECT MemberID, WLID FROM WhiteListRecData WHERE WLID IN (SELECT WID FROM WhiteListData WHERE Title IN ('All'))
        """)
        return [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

    def getJDSN():
        cursor = connection.cursor()
        query = cursor.execute("""
            SELECT DISTINCT JDSN FROM CTData
        """, [])
        return [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]


class PermissionsView(APIView):
    def get(self, request, id):
        member = Member.objects.get(pk=id)
        serializer = MemberSerializer(member)
        userData = serializer.data

        position = ['Member']
        jdsn = []
        eduList = []
        csamList = []
        allList = []

        WhiteListResult = WhiteList.getWhiteList()
        JdsnResult = WhiteList.getJDSN()

        for row in JdsnResult:
            jdsn.append(row['JDSN'])

        for row in WhiteListResult:
            match row['WLID']:
                case "3":
                    eduList.append(row['MemberID'])
                case "2":
                    csamList.append(row['MemberID'])
                case "1":
                    allList.append(row['MemberID'])

        if userData['id'] in jdsn:
            position.append('JDSN')

        if (
            userData['internal_position'] == "1" and userData['group_imwy'] != 'Center Dept'
            or (userData['internal_position'] == "1" and userData['group_imwy'] == 'Center Dept' and userData['internal_position'] == 'Leader')

            or (userData['inner_dept'] == 'Evangelism' and userData['internal_position'] == 'Secretary' )
            or (userData['membergroup'] == 'Department' and userData['tgw'] == "1" and userData['condition'] == 'Active')
            or (userData['membergroup'] == 'Hangul' )
            or (userData['membergroup'] == 'P0' and userData['tgw'] == "1" and userData['condition'] == 'Active')
        ):
            position.append('Leader')

        if (
            userData['uid'] in allList
                or (userData['membergroup'] == 'Department' and userData['tgw'] == "1" and userData['condition'] == 'Active')
                or (userData['membergroup'] == 'Hangul' )
                or (userData['membergroup'] == 'P0' and userData['tgw'] == "1" and userData['condition'] == 'Active')
        ):
            position.append('Dept')

        if userData['internal_position'] == "1" and userData['internal_position'] == "2" and userData['uid'] in allList and userData['id'] in JdsnResult and 'Leader' in position:
            position.append('EVLeader')

        if (
            userData['bbt'] is True or userData['uid'] in allList
        ):
            position.append('bbt')

        if (
            userData['uid'] in csamList or userData['uid'] in allList
        ):
            position.append('CSAM')

        if (
            userData['uid'] in eduList or userData['uid'] in allList
        ):
            position.push('Edu')

        return Response(position)