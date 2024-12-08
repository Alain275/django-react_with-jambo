from django.urls import path,include
# from rest_framework.routers import SimpleRouter
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ChallengeViewSet,BookmarkChallengeContainerViewSet,ReviewViewSet,BookmarkChallengeItemViewSet,OrderingFeedBackViewSet
from user.views import StudentViewSet
# from pprint import pprint
# urlpatterns = [
#     path('',include(router.urls)),
#     path('hero_page', views.hero_world_view),
#     # path('challenge/', views.ChallengeList.as_view()),
#     # path('challenge/<int:pk>/', views.ChallengeDetail.as_view()),
# ]

# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('challenges',ChallengeViewSet,basename='challenges')
router.register('bookmark',BookmarkChallengeContainerViewSet,basename='bookmark')
router.register('students',StudentViewSet,basename='student')
router.register('ordersfeedback',OrderingFeedBackViewSet,basename='ordersfeedback')
challeng_router = routers.NestedSimpleRouter(router,'challenges', lookup='challenge')
challeng_router.register('review', ReviewViewSet, basename='challenge-review')
BookmarkChallengeContainer_router = routers.NestedSimpleRouter(router,'bookmark', lookup='bookmark')
BookmarkChallengeContainer_router.register(
    'BookmarkChallengeItem',
    BookmarkChallengeItemViewSet,
    basename='BookmarkChallengeContainer-BookmarkChallengeItem'
)
# pprint(router.urls)

urlpatterns = router.urls + challeng_router.urls+BookmarkChallengeContainer_router.urls

# alternative:


# urlpatterns = [
#     path('', include(router.urls)),
#     path('hero_page', views.hero_world_view),
#     path('', include(challeng_router.urls)),
# ]

