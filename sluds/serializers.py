from models import Users, User_OpenAuth, User_LocalAuth
from rest_framework import serializers
from datetime import datetime

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('UserID','NickName','LevelID','AccountPic_URL','SelfIntroduction','Gender','LocationProvince','LocationCity','CTime','MTime')
    def create(self, validated_data):
        return  Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.NickName = validated_data.get('NickName', instance.NickName)
        instance.AccountPic_URL = validated_data.get('AccountPic_URL', instance.AccountPic_URL)
        instance.SelfIntroduction = validated_data.get('SelfIntroduction', instance.SelfIntroduction)
        instance.Gender = validated_data.get('Gender', instance.Gender)
        instance.LocationProvince = validated_data.get('LocationProvince', instance.LocationProvince)
        instance.LocationCity = validated_data.get('LocationCity', instance.LocationCity)
        instance.MTime = datetime.utcnow()
        instance.save()
        return instance

class User_OpenAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_OpenAuth
        fields = ('ID','UserID','NickName','OAuthType','OAuthID','OAuth_Access_Token',
                'OAuth_Refresh_Access_Token','OAuth_Expires','Scope','AccountPic_URL',
                'Gender','Country','Province','City','CTime','MTime')

class User_LocalAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        module = User_LocalAuth
        fields = ('ID','UserID','LAuthType','UserName','Password','CTime','MTime')

