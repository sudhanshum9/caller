from rest_framework import serializers

from truecaller import models


class UserProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.UserProfile
        fields = ('id','phoneno', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        
        user = models.UserProfile.objects.create_user(
            phoneno= validated_data['phoneno'],
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)



class UserContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserContacts
        fields = ("id",'user_profile','phoneno','name','email')
        extra_kwargs = {'user_profile':{'read_only': True}}



class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Spam
        fields = '__all__'


class GlobalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GlobalData
        fields = ('user_profile','usercontact','spam')

        


    user_profile = UserProfileSerializer(many=True,read_only=True)
    usercontact= UserContactSerializer(many=True,read_only=True)
    spam = SpamSerializer(many=True,read_only=True)