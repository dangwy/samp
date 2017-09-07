from .models import Users, User_OpenAuth, User_LocalAuth
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone

#class UsersSerializer(serializers.HyperlinkedModelSerializer):
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        #fields = ('UserID','NickName','LevelID','AccountPic_URL','SelfIntroduction','Gender','LocationProvince','LocationCity','CTime','MTime')
        fields = ('UserID', 'NickName', 'LevelID', 'AccountPic_URL', 'SelfIntroduction', 'Gender', 'LocationProvince',
                  'LocationCity')

    def create(self, validated_data):
        return  Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance.UserID = validated_data.get('UserID', instance.UserID)
        instance.NickName = validated_data.get('NickName', instance.NickName)
        instance.AccountPic_URL = validated_data.get('AccountPic_URL', instance.AccountPic_URL)
        instance.SelfIntroduction = validated_data.get('SelfIntroduction', instance.SelfIntroduction)
        instance.Gender = validated_data.get('Gender', instance.Gender)
        instance.LocationProvince = validated_data.get('LocationProvince', instance.LocationProvince)
        instance.LocationCity = validated_data.get('LocationCity', instance.LocationCity)
        instance.MTime = timezone.now()
        instance.save()
        return instance

    def __repr__(self):
        return u'<Users: %d, %s>' % (self.UserID, self.NickName)

class User_OpenAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_OpenAuth
        fields = ('ID','UserID','NickName','OAuthType','OAuthID','OAuth_Access_Token',
                'OAuth_Refresh_Access_Token','OAuth_Expires','Scope','AccountPic_URL',
                'Gender','Country','Province','City','CTime','MTime')

    def create(self, validated_data):
        return User_OpenAuth.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.NickName = validated_data.get('NickName', instance.NickName)
        instance.OAuthType = validated_data.get('OAuthType', instance.OAuthType)
        instance.OAuthID = validated_data.get('OAuthID', instance.OAuthID)
        instance.OAuth_Access_Token = validated_data.get('OAuth_Access_Token', instance.OAuth_Access_Token)
        instance.OAuth_Refresh_Access_Token = validated_data.get('OAuth_Refresh_Access_Token', instance.OAuth_Refresh_Access_Token)
        instance.OAuth_Expires = validated_data.get('OAuth_Expires', instance.OAuth_Expires)
        instance.Scope = validated_data.get('Scope', instance.Scope)
        instance.AccountPic_URL = validated_data.get('AccountPic_URL', instance.AccountPic_URL)
        instance.Gender = validated_data.get('Gender', instance.Gender)
        instance.Country = validated_data.get('Country', instance.Country)
        instance.Province = validated_data.get('Province', instance.Province)
        instance.City = validated_data.get('City', instance.City)
        instance.MTime = timezone.now()
        instance.save()
        return instance

class User_LocalAuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        module = User_LocalAuth
        fields = ('ID','UserID','LAuthType','UserName','Password','CTime','MTime')

    def create(self, validated_data):
        return User_LocalAuth.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.LAuthType = validated_data.get('LAuthType', instance.LAuthType)
        instance.UserName = validated_data.get('UserName', instance.UserName)
        instance.Password = validated_data.get('Password', instance.Password)
        instance.IsActive = validated_data.get('IsActive', instance.IsActive)
        instance.MTime = timezone.now()
        instance.save()
        return instance

