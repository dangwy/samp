from models import Users, User_OpenAuth, User_LocalAuth
from rest_framework import serializers

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('UserID','NickName','LevelID','AccountPic_URL','SelfIntroduction','Gender','LocationProvince','LocationCity','CTime','MTime')

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

# class ReqBodyPrefixSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         fields = ('version','action','userid')