from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError


class TokenClass :
    @property
    def tokens (self) :
        user = self.user
        tokens = RefreshToken.for_user(user)
        return {
            'token' : str(tokens.access_token)
        }

class LoginSerializer (serializers.Serializer, TokenClass) : 
    phonenumber = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        phonenumber = attrs['phonenumber']
        password = attrs['password']

        try : 
            self.user = User.objects.get(phonenumber=phonenumber)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid phonenumber"
            })
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : "invalid password"
            })

        return attrs
    
class RegisterSerializer(serializers.ModelSerializer, TokenClass) :
    class Meta:
        model = User
        fields = ('full_name', 'phonenumber', 'password', )

    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        return self.user
