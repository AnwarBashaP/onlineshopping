from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from LandingPage.serializer import UserLoginSerializer
from .authentications.tokenexpires import token_expire_handler, expires_in
from .models import User
from .serializer import UserSerializer


@api_view(['POST',])
@permission_classes((AllowAny,))
def register_view(request):
    print(request.data)
    if request.method ==  'POST':
        serializer = UserSerializer(data= request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = 'Successfully registered a new user'
            data['email'] = user.email
            data['username'] =  user.userName
            data['status']= 'pass'
            token,created = Token.objects.get_or_create(user= user)
            request.session['token'] = token.key
            request.session['user'] = user.userName
            data['token'] =  token.key
        else:
            data =  serializer.errors
        print(data)
        return Response(data)

@permission_classes((AllowAny,))
class LoginApiview(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            tokengenerate = User.objects.get(email = request.data['email'],is_active = True)
            Uid = User.objects.filter(email = request.data['email'],is_active = True).values('UserID','userName','email').first()

        # token, created = Token.objects.create(user=Uid['UserID'])


        Token.objects.filter(user=tokengenerate).delete()
        token,create = Token.objects.get_or_create(user= tokengenerate)

        # token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)  # The implementation will be described further
        request.session['token'] = token.key
        request.session['user'] = Uid['userName']
        data = {}
        data['expires_in'] =  expires_in(token)
        data['User_id'] =Uid['userName']
        data['email'] =Uid['email']
        data['token'] =token.key
        return Response(data)