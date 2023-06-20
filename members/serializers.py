from rest_framework import serializers
from . import models
from .models import Memberdata as Member
from forms.models import Memberlogindata

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','preferred_name', 'membergroup','internal_position','inner_dept','group_imwy','region','tgw','bbt','condition','uid']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        member_count = serializers.IntegerField(
            source='member_set.count',
            read_only=True
        )

    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class MemberLoginDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Memberlogindata
        fields = ['id', 'mid', 'logintime', 'uid']

    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
