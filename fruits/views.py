import email
import imp
from lib2to3.pgen2 import token
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
# from .serializers import UserSerializer, MemberSerializer
# from .models import Memberuserdata as User
# from .models import Memberdata as Member
# from .models import Whitelistdata as WL
# from .models import Whitelistrecdata as WLR
from django.db.models import Q
from django.db import connection
import jwt, datetime
from django.http import JsonResponse
import json

class getBbtStudentsView(APIView):
    def get(self,request,fruitKey):
        cursor = connection.cursor()
        query = cursor.execute("""
            SELECT F.*
                ,M1.Group_IMWY L1_Dept
                ,M2.Group_IMWY L2_Dept
            FROM FruitData F
            LEFT JOIN MemberData M1 ON F.F1_ID = M1.UID
            LEFT JOIN MemberData M2 ON F.F2_ID = M2.UID
            WHERE F.Fruitkey = %s
            ORDER BY LastUpdate DESC;
        """, [fruitKey])
        return [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

class getPerBBTView(APIView):
    def get(self,request,seasonid):
        cursor = connection.cursor()
        cursor.execute("exec spBBTAPGetBBTs {0}".format(seasonid))
        results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

        return Response(results)

class getPerGroupView(APIView):
    def get(self,request,region):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT DISTINCT MemberGroup Grp
            ,ISNULL((
                    SELECT SUM(F.L1_Points)
                    FROM BBData AS B
                    LEFT JOIN FruitData AS F ON F.UID = B.UID
                    LEFT JOIN MemberData AS M1 ON B.L1_ID = M1.UID
                    WHERE M1.MemberGroup = M.MemberGroup
                        AND M1.Region = M.Region
                        AND B.Stat_Abbr IN (
                            'P'
                            ,'FE'
                            ,'ONG'
                            ,'STB'
                            ,'CT'
                            ,'CCT'
                            ,'SUB'
                            )
                    ), 0) + ISNULL((
                    SELECT SUM(F.L2_Points)
                    FROM BBData AS B
                    LEFT JOIN FruitData AS F ON F.UID = B.UID
                    LEFT JOIN MemberData AS M2 ON B.L2_ID = M2.UID
                    WHERE M2.MemberGroup = M.MemberGroup
                        AND M2.Region = M.Region
                        AND B.Stat_Abbr IN (
                            'P'
                            ,'FE'
                            ,'ONG'
                            ,'STB'
                            ,'CT'
                            ,'CCT'
                            ,'SUB'
                            )
                    ), 0) AS 'Active'
            ,ISNULL((
                    SELECT SUM(F.L1_Points)
                    FROM BBData AS B
                    LEFT JOIN FruitData AS F ON F.UID = B.UID
                    LEFT JOIN MemberData AS M1 ON B.L1_ID = M1.UID
                    WHERE M1.MemberGroup = M.MemberGroup
                        AND M1.Region = M.Region
                    ), 0) + ISNULL((
                    SELECT SUM(F.L2_Points)
                    FROM BBData AS B
                    LEFT JOIN FruitData AS F ON F.UID = B.UID
                    LEFT JOIN MemberData AS M2 ON B.L2_ID = M2.UID
                    WHERE M2.MemberGroup = M.MemberGroup
                        AND M2.Region = M.Region
                    ), 0) AS 'Total'
        FROM (
            SELECT MemberGroup
                ,Inner_Dept
                ,ID
                ,Region
            FROM MemberData
            WHERE Region = %s
                AND MemberGroup != ''
            ) AS M;
        """,[region])
        return [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

class getFruitListView(APIView):
        def get(self,request,id):
            dateFrom = request.query_params.get('dateFrom')
            dateTo = request.query_params.get('dateTo')
            cursor = connection.cursor()
            cursor.execute("""
                DECLARE @fisher_id INT = %s
                    ,@dateFrom DATETIME2 = %s
                    ,@dateTo DATETIME2 = %s

                SELECT F.UID
                    ,DATEDIFF(day, CAST(GETDATE() AS DATE), F.UnlockDate) LockDays
                    ,F.Stage
                    ,F.LastUpdate
                    ,F.FishName
                    ,F.Stage_P
                    ,F.Stage_M
                    ,F.Stage_F
                    ,F.FruitStatus AS STATUS
                    ,F.F1_Points AS F1P
                    ,F.F2_Points AS F2P
                    ,F.A1_Points AS M1P
                    ,F.A2_Points AS M2P
                    ,F.PP1_Points AS PP1P
                    ,F.PP2_Points AS PP2P
                    ,F.L1_Points AS P1P
                    ,F.L2_Points AS P2P
                    ,F1.MemberGroup AS F1G
                    ,F1.PREFERRED_NAME AS F1_Name
                    ,F2.MemberGroup AS F2G
                    ,F2.PREFERRED_NAME AS F2_Name
                    ,M1.MemberGroup AS M1G
                    ,M1.PREFERRED_NAME AS M1_Name
                    ,M2.MemberGroup AS M2G
                    ,M2.PREFERRED_NAME AS M2_Name
                    ,PP1.MemberGroup AS PP1G
                    ,PP1.PREFERRED_NAME AS PP1_Name
                    ,PP2.MemberGroup AS PP2G
                    ,PP2.PREFERRED_NAME AS PP2_Name
                    ,P1.MemberGroup AS P1G
                    ,P1.PREFERRED_NAME AS P1_Name
                    ,P2.MemberGroup AS P2G
                    ,P2.PREFERRED_NAME AS P2_Name
                    ,BB.STATUS AS BB_Status
                    ,ISNULL(BB.Stat_Abbr, '') AS StAbbr
                    ,BB.Label AS Label
                    ,L1.MemberGroup AS L1G
                    ,L1.PREFERRED_NAME AS L1_Name
                    ,L2.MemberGroup AS P2G
                    ,L2.PREFERRED_NAME AS L2_Name
                    ,F.Proceedable
                FROM dbo.FruitData AS F
                LEFT JOIN MemberData AS F1 ON F.F1_ID = F1.UID
                LEFT JOIN MemberData AS F2 ON F.F2_ID = F2.UID
                LEFT JOIN MemberData AS M1 ON F.Attendee_1_ID = M1.UID
                LEFT JOIN MemberData AS M2 ON F.Attendee_2_ID = M2.UID
                LEFT JOIN MemberData AS PP1 ON F.PP1_ID = PP1.UID
                LEFT JOIN MemberData AS PP2 ON F.PP2_ID = PP2.UID
                LEFT JOIN MemberData AS P1 ON F.L1_ID = P1.UID
                LEFT JOIN MemberData AS P2 ON F.L2_ID = P2.UID
                LEFT JOIN BBData AS BB ON F.UID = BB.UID
                LEFT JOIN MemberData AS L1 ON BB.L1_ID = L1.UID
                LEFT JOIN MemberData AS L2 ON BB.L2_ID = L2.UID
                WHERE (
                        CAST(F.LastUpdate AS DATE) BETWEEN @dateFrom
                            AND @dateTo
                        )
                    AND (
                        (
                            F.F1_ID = @fisher_id
                            OR F.F2_ID = @fisher_id
                            )
                        OR (
                            F.Attendee_1_ID = @fisher_id
                            OR F.Attendee_2_ID = @fisher_id
                            )
                        OR (
                            F.PP1_ID = @fisher_id
                            OR F.PP2_ID = @fisher_id
                            )
                        OR (
                            F.L1_ID = @fisher_id
                            OR F.L2_ID = @fisher_id
                            )
                        )
                ORDER BY F.LastUpdate DESC;
            """, [id, dateFrom, dateTo])
            return [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

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