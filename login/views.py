import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

# Create your views here.
class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            login_user = Post.objects.filter(M_id=data['M_id'])

            if not login_user.exists() or login_user[0].M_pw != data['M_pw']:
                return JsonResponse({'MESSAGE' : 'INVALID_USER'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)

        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=200)