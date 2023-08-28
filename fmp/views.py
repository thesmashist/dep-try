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

class EVStatsOverall(APIView):
    # @method_decorator(cache_page(60*60*2))
    def get(self,request,id):
            member = Member.objects.get(pk=id)
            serializer = MemberSerializer(member)

            cursor = connection.cursor()
            query = cursor.execute("exec spTotalEvStats {0}".format(serializer.data['uid']))
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

            BB = {}
            ME = []
            P = []
            FA = []
            FE = []
            STB = []
            ONG = []

        # for row in BBResults:
        #     print(row)
        #     match row['STATUS']:
        #         case "Missed Education":
        #             ME.append(row)
        #         case "Picking":
        #             P.append(row)
        #         case "Fallen":
        #             FA.append(row)
        #         case "First Education":
        #             FE.append(row)
        #         case "Stable":
        #             STB.append(row)
        #         case "Ongoing Education":
        #             ONG.append(row)


        # BB['ME'] = ME
        # BB['FA'] = FA
        # BB['FE'] = FE
        # BB['P'] = P
        # BB['ONG'] = ONG
        # BB['STB'] = STB


            return Response(results)

class EVStats(APIView):
    def get(self,request,id):
            member = Member.objects.get(pk=id)
            serializer = MemberSerializer(member)

            cursor = connection.cursor()
            query = cursor.execute("exec spWeeklyEvStats {0}".format(serializer.data['uid']))
            results = [ dict( zip( [column[0] for column in cursor.description] , record ) ) for record in cursor.fetchall()]

            return Response(results)