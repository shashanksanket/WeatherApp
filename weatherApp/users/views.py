from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import permissions
from rest_framework.response import Response

class AuthView(APIView):

	allowed_methods = ['post', 'delete']

	def get_permissions(self):
		if self.request.method == "DELETE":
			self.permission_classes = [permissions.IsAuthenticated]
		else:
			self.permission_classes = [permissions.AllowAny]
		return [permission() for permission in self.permission_classes]

	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		if username is None or password is None:
			return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
		user = authenticate(username=username, password=password)
		if not user:
			return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
		token, _ = Token.objects.get_or_create(user = user)
		return Response({'token': token.key}, status=HTTP_200_OK)

	def delete(self, request):
		try: 
			token = Token.objects.get(user=request.user)
		except Token.DoesNotExist:
			return  Response({'error': 'Invalid Token'}, status=HTTP_404_NOT_FOUND)
		token.delete()
		return Response({'message': "User logged out successfully"})
   

