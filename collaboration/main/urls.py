from django.urls import path,include
# from rest_framework.routers import SimpleRouter
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
from .views import ChallengeViewSet,ReviewViewSet
# from pprint import pprint

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('Challenges',views.ChallengeViewSet)
challeng_router = routers.NestedSimpleRouter(router,'Challenges', lookup='Challenge')
challeng_router.register('review', views.ReviewViewSet, basename='challenge-review')
# pprint(router.urls)

urlpatterns = router.urls + challeng_router.urls

# alternative:


# urlpatterns = [
#     path('', include(router.urls)),
#     path('hero_page', views.hero_world_view),
#     path('', include(challeng_router.urls)),
# ]

# urlpatterns = [
#     path('',include(router.urls)),
#     path('hero_page', views.hero_world_view),
#     # path('challenge/', views.ChallengeList.as_view()),
#     # path('challenge/<int:pk>/', views.ChallengeDetail.as_view()),
# ]
