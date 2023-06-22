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

class EVStats(APIView):
    def get(self,request,id):
            member = Member.objects.get(pk=id)
            serializer = MemberSerializer(member)

            cursor = connection.cursor()
            query = cursor.execute("""
                DECLARE @Fisher_id VARCHAR(6) = %s
                ,@ThisWeek DATETIME2 = %s
                ,@ThisDate DATETIME2 = %s

            SELECT SUM(F1_Points) AS F1
                ,SUM(F2_Points) AS F2
                ,SUM(A1_Points) AS A1
                ,SUM(A2_Points) AS A2
                ,SUM(PP1_Points) AS PP1
                ,SUM(PP2_Points) AS PP2
                ,SUM(L1_Points) AS L1
                ,SUM(L2_Points) AS L2
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
                                P_TIME BETWEEN @ThisDate AND
                                @ThisWeek

                                )
                            OR (
                                PP_TIME BETWEEN @ThisDate AND
                                @ThisWeek
                                )
                            OR (
                                M_TIME BETWEEN @ThisDate AND
                                @ThisWeek
                                )
                            OR (
                                F_TIME BETWEEN @ThisDate AND
                                @ThisWeek
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
            """, [serializer.data['uid'],'2023-06-20 20:36:00',  '2023-05-17 20:36:00'])
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

            return Response(results)