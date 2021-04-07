from rest_framework import serializers, status

from Ecommerce import CustomValidationError
from .models import User



class UserSerializer(serializers.ModelSerializer):
    cnfrmpassword = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model =  User
        fields = ('email','userName','password','cnfrmpassword')

    def save(self, **kwargs):
        user = User(email= self.validated_data['email'],userName= self.validated_data['userName'],is_member= True,is_active = True)

        password =  self.validated_data['password']
        password2 =  self.validated_data['cnfrmpassword']

        if password != password2:
            raise CustomValidationError( "Password didn't match !","Password", status_code=status.HTTP_401_UNAUTHORIZED)
            # raise serializers.ValidationError({"password":"Password must match!"})
        user.set_password(password)
        user.save()
        return user