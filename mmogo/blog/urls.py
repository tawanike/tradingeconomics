from django.conf.urls import url
from mmogo.blog import views



urlpatterns = [
	url(r'', views.index, name="blog_home")
]
