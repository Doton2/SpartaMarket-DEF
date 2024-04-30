from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','Nick_name','birthday','gender','content')
        

    def create(self , vlisated_data):
        user = User(
            username = vlisated_data['username'],
            email = vlisated_data['email'],
            name = vlisated_data['name'],
            Nick_name = vlisated_data['Nick_name'],
            birthday = vlisated_data['birthday'],
            gender = vlisated_data['gender'],
            content = vlisated_data['content']
        )
        user.set_password(vlisated_data['password'])
        user.save()
        return user
    
