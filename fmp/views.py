from django.shortcuts import render
from rest_framework import generics, mixins
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Q
from django.db import connection
from . import serializers, models
from django.db import connection
from members import models, serializers
from members.models import Memberdata as Member
from members.serializers import MemberSerializer

class EVSeason(APIView):
    def get(self, request, region, department):
            if(department == 'MW'): department = 'M&W Dept'

            cursor = connection.cursor()
            query = cursor.execute("""
                SELECT TOP 1 ID
                FROM EVSeason
                WHERE StartDate < GETDATE()
                    AND Region = %s
                    AND Dept = %s
                ORDER BY ID DESC
            """, [region, department])
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

            return Response(results)

class EVStats(APIView):
    def get(self,request,id):
            member = Member.objects.get(pk=id)
            serializer = MemberSerializer(member)

            cursor = connection.cursor()
            query = cursor.execute("""
                DECLARE @Fisher_id VARCHAR(6) = %s

                DECLARE @ThisDate DATETIME2 = CAST((
                SELECT SYSDATETIMEOFFSET() AT TIME ZONE 'AUS Eastern Standard Time'
                        ) AS DATE);
                DECLARE @ThisWeek DATETIME2 = CASE
                        WHEN DATEPART(WEEKDAY, @ThisDate) BETWEEN 2
                                AND 4
                            THEN (
                                    SELECT DATEADD(wk, DATEDIFF(wk, 0, @ThisDate) - 1, 3)
                                    )
                        ELSE (
                                SELECT DATEADD(wk, DATEDIFF(wk, 0, @ThisDate), 3)
                                )
                        END;

            SELECT ISNULL(SUM(F1_Points),0) AS F1
                ,ISNULL(SUM(F2_Points),0) AS F2
                ,ISNULL(SUM(A1_Points),0) AS A1
                ,ISNULL(SUM(A2_Points),0) AS A2
                ,ISNULL(SUM(PP1_Points),0) AS PP1
                ,ISNULL(SUM(PP2_Points),0) AS PP2
                ,ISNULL(SUM(L1_Points),0) AS L1
                ,ISNULL(SUM(L2_Points),0) AS L2
            FROM dbo.FruitData f
            LEFT JOIN BBData AS BB ON f.FruitKey = BB.FruitKey
            WHERE (
                    (
                        (
                            f.L2_ID = @Fisher_id
                            OR f.L1_ID = @Fisher_id
                            )
                        OR (
                            f.PP1_ID = @Fisher_id
                            OR f.PP2_ID = @Fisher_id
                            )
                        OR (
                            f.F2_ID = @Fisher_id
                            OR f.F1_ID = @Fisher_id
                            )
                        OR (
                            f.Attendee_1_ID = @Fisher_id
                            OR f.Attendee_2_ID = @Fisher_id
                            )
                    ) AND (
                            (
                                P_TIME BETWEEN @ThisWeek AND
                                @ThisDate

                                )
                            OR (
                                PP_TIME BETWEEN @ThisWeek AND
                                @ThisDate
                                )
                            OR (
                                M_TIME BETWEEN @ThisWeek AND
                                @ThisDate
                                )
                            OR (
                                F_TIME BETWEEN @ThisWeek AND
                                @ThisDate
                            )
                        )
                    )
                OR (
                    (
                        F2_ID = @Fisher_id
                        OR F1_ID = @Fisher_id
                        )
                    AND BB.Stat_Abbr IN (
                        SELECT value
                        FROM STRING_SPLIT('Ong,FE,STB,CT,CCT,ME,NCT', ',')
                        )
                    AND Completed = 0
                    )
            """, [serializer.data['uid']])
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

            return Response(results)