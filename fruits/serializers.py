from asyncio import constants
import imp
from rest_framework import serializers
from .models import Memberuserdata as User
from .models import Memberdata as Member

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','preferred_name', 'membergroup','internal_position','inner_dept','group_imwy','region','tgw','bbt','condition']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
        