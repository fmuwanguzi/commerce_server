from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken 
from .models import Product

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
      
    class Meta:
        model = User
        # '_id' field has been added just to keep consistant with the id on the front end
        fields = ['id','_id' ,'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff
    
    def get_name(self, obj):
        name = obj.first_name
        #if a name isn't available we will use the email
        if name == '':
            name = obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id' ,'username', 'email', 'name', 'isAdmin', 'token']
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
                       
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        