# Thirdparty imports
from django.urls import include, path
from rest_framework import routers

# Projects imports
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

# V1_router settings
v1_router = routers.DefaultRouter()
v1_router.register("follow", FollowViewSet, basename="follow")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(v1_router.urls)),
]
