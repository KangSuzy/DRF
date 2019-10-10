from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
import requests
import json
# Create your views here.

#CBV
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
#Kakao api
url = "https://dapi.kakao.com/v2/search/web"
queryString = {"query" : "덕성여자대학교"}
header = {"Authorization" : "KakaoAK 69c1aa58f5aa716651312afb2febb1d6"}
r = requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))
'''
#kakao api
url = "https://kapi.kakao.com/v1/translation/translate"
queryString = {"query" : "사과는 맛나~",
    "src_lang" : "kr",
    "target_lang" : "en" }
header = {"Authorization" : "KakaoAK 69c1aa58f5aa716651312afb2febb1d6"}
r = requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))