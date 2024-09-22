from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
import rest_framwork 


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FollowUserView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UnfollowUserView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer


