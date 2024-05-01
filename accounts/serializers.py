from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','Nick_name','birthday','gender','content')
        

    def create(self , vlisated_data):
        user = User(**vlisated_data)
        user.set_password(vlisated_data['password'])
        user.save()
        return user
    
    