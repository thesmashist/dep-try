
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
from .models import Memberdata as Member
from .serializers import MemberSerializer


# Create your views here.
class MemberAPIView(APIView):
    def get(self, request, id):
        member = Member.objects.get(pk=id)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

class MemberLogin(APIView):
    def get(self, request, id):
        Memberlogindata.objects.filter(id = id).update(logintime = timezone.now())
        member = Memberlogindata.objects.get(pk=id)
        serializer = MemberLoginDataSerializer(member)
        return Response(serializer.data)

class MemberByRegion(generics.ListAPIView):
        queryset = Member.objects.all()
        serializer_class = MemberSerializer
        filter_backends = [DjangoFilterBackend]
        filter_fields = ['region']

        @method_decorator(cache_page(60*60*2))
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)


class MemberList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
        queryset = Member.objects.all()
        serializer_class = MemberSerializer

        @method_decorator(cache_page(60*60*2))
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)