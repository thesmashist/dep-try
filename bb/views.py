from django.shortcuts import render
from lib2to3.pgen2 import token
from unittest import result
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import Memberuserdata as User, Memberdata as Member
from django.db.models import Q
from django.db import connection
import jwt, datetime
from django.http import JsonResponse
import json

# Create your views here.
class BBTAPGetBBTData(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')
        region = request.data['region']
        season = request.data['season']
        # groupCursor = connection.cursor()
        bbtCursor = connection.cursor()

        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id)
        try:
            # groupCursor.execute("SELECT DISTINCT MemberGroup AS 'Group', Inner_Dept AS 'Inner Department', Group_IMWY Department, (SELECT TOP 1 PREFERRED_NAME FROM MemberData WHERE Internal_Position = 1 AND MemberGroup = M.MemberGroup) AS GYJN FROM MemberData M WHERE Region = %s",(region,))
            # groups = [ dict( zip( [column[0] for column in groupCursor.description] , record ) ) for record in groupCursor.fetchall()]
            bbtCursor.execute('EXEC spBBTAPGetBBTs %s, %s', (season, region))
            bbts = [ dict( zip( [column[0] for column in bbtCursor.description] , record ) ) for record in bbtCursor.fetchall()]
            result = {
                # 'Groups': groups,
                'BBTs': bbts
            }
        finally:
            # groupCursor.close()
            bbtCursor.close()

        return Response(result)

# Create your views here.
class BBTAPGetStudentData(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')
        season = request.data['season']
        studentCursor = connection.cursor()

        if not token:
            raise AuthenticationFailed('Unauthorized!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id)
        try:
            studentCursor.execute('EXEC spGetBBStudentList %s',(season,))
            seasons = [ dict( zip( [column[0] for column in studentCursor.description] , record ) ) for record in studentCursor.fetchall()]
            result = {
                # 'Groups': groups,
                'Students': seasons,
            }
        finally:
            # groupCursor.close()
            studentCursor.close()

        return Response(result)

# Create your views here.
class BBTAPGetTotalStats(APIView):
    def post(self, request):
        token = request.COOKIES.get('token')
        season = request.data['season']
        totalsCursor = connection.cursor()
        regionsCursor = connection.cursor()
        deptsCursor = connection.cursor()
        groupsCursor = connection.cursor()

        if not token:
            raise AuthenticationFailed('Unauthorized!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthorized!')
        user = Member.objects.filter(id = payload['id']).first()
        print(user.id)
        try:
            totalsCursor.execute('EXEC spBBTAPGetAllTotals %s',(season,))
            totals = [ dict( zip( [column[0] for column in totalsCursor.description] , record ) ) for record in totalsCursor.fetchall()]
            regionsCursor.execute('EXEC spBBTAPGetRegionTotals')
            regions = [ dict( zip( [column[0] for column in regionsCursor.description] , record ) ) for record in regionsCursor.fetchall()]
            deptsCursor.execute('EXEC spBBTAPGetPerDept %s',(season,))
            depts = [ dict( zip( [column[0] for column in deptsCursor.description] , record ) ) for record in deptsCursor.fetchall()]
            groupsCursor.execute('EXEC spBBTAPGetPerGroup %s',(season,))
            groups = [ dict( zip( [column[0] for column in groupsCursor.description] , record ) ) for record in groupsCursor.fetchall()]
            result = {
                'Groups': groups,
                'Totals': totals,
                'Depts': depts,
                'Regions': regions,
            }
        finally:
            totalsCursor.close()
            regionsCursor.close()
            deptsCursor.close()
            groupsCursor.close()

        return Response(result)
