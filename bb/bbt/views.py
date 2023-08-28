from rest_framework import generics, mixins
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Q
from django.db import connection
from members import serializers, models
from members.models import Memberdata as Member
from members.serializers import MemberSerializer

class BBTList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
        queryset = Member.objects.filter(bbt = 1, btm__isnull=False).exclude(Q(region = "Perth"))
        serializer_class = MemberSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)