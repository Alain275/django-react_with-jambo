# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from rest_framework import status
from rest_framework.response import Response 
# from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,ListModelMixin,DestroyModelMixin
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from .permissions import IsAdminOrReadOnly


# we use this if we want to list only the data
# there is update , delete or create data
# from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models
from .serializers import  ChallengeSerializer,\
ReviewSerializer,\
BookmarkChallengeContainerSerializer,\
BookmarkChallengeItemSerializer,\
AddBookmarkChallengeItemSerializer,\
UpdateBookmarkChallengeItemSerializer,\
OrderingFeedBackSerializer,\
CreateOrderingFeedBackSerializer,\
UpdateOrderingFeedBackSerializer

# @api_view()
# def hero_world_view(request):
#     # queryset = User.objects.filter(id__range=(7, 20)).order_by('-id')  # Adjust the range as needed
#     # context = {
#     #     'users': queryset  # Passing the queryset to the template
#     # }
#     # return render(request, 'index.html', context)

#     return Response("okay")

#  this the similar implimantation using api function based view
# _________________________________________________________________

# @api_view(['GET','POST'])
# def challenge_list(request):
#     if request.method == 'GET':
#         queryset = models.Challenges.objects.all()
#         serializer = ChallengeSerializer(queryset,many=True)
#         return Response (serializer.data)
#     elif request.method == 'POST':
#         serializer = ChallengeSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response('okay')
#         # else:
#         #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# this the class based view for the same implimantation
# _________________________________________________________________



# class ChallengeList(APIView):
#     def get(self,request):
#         queryset = models.Challenges.objects.all()
#         serializer = ChallengeSerializer(queryset,many=True)
#         return Response (serializer.data)

#     def post(self,request):
#         serializer = ChallengeSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)



# and now this is the implimantation of mixins using generic view for geting the same implimantation
# ____________________________________________________________________________________________________


# NB:any mixin here can be overriden : so it lecturer called customizing generic view 


# class ChallengeList(ListCreateAPIView):
#     queryset = models.Challenges.objects.all()
#     serializer_class = ChallengeSerializer


    # def get_queryset(self):
    #     return models.Challenges.objects.all()
   
#    this method some times gets error

    # def get_serializer(self, *args, **kwargs):
    #     return ChallengeSerializer


# @api_view(['GET','POST','DELETE'])
# def challenge_detail(request,id):
#     challenge = get_object_or_404(models.Challenges,pk=id)
#     if request.method == 'GET':
#         serializer = ChallengeSerializer(challenge)
#         return Response (serializer.data)
#     elif request.method == 'POST':
#         serializer = ChallengeSerializer(challenge,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     elif request.method =='DELETE':
#         challenge.delete()
#         return Response("deleted")


# and here is the same implimanation useng generic api view
# _____________________________________________________________

# NB: here  on delete method we have used id in urls but for generic view we have to use pk in urls
#     so to solve it we set our lookup_field = id or stick to default django comvation of renaming 
# it to pk but when overriding any method eg PUT , GET , UPDATE OR DELETE


# class ChallengeDetail(RetrieveUpdateDestroyAPIView):
#     queryset = models.Challenges.objects.all()
#     serializer_class = ChallengeSerializer  


# okay now lets now puts the 2 classes(ChallengeList and ChallengeDetail) in one view set
# _________________________________________________________________________________________  

class ChallengeViewSet(ModelViewSet):
    queryset = models.Challenges.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChallengeSerializer
    pagination_class = PageNumberPagination # also here we can define this class for our self and the warning gone
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['user__id']  # we can also define a class outside this and perfom all actions for filtering
    search_fields = ['challenge_name']
    ordering_fields = ['id']

   


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = models.Review.objects.all()
    permission_classes = [IsAuthenticated]

class BookmarkChallengeContainerViewSet(CreateModelMixin,
                                        ListModelMixin,
                                        RetrieveModelMixin,
                                        DestroyModelMixin,
                                        GenericViewSet):
    serializer_class = BookmarkChallengeContainerSerializer
    queryset = models.BookmarkChallengeContainer.objects.all()
    permission_classes = [IsAuthenticated]

class BookmarkChallengeItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post','patch','delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBookmarkChallengeItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateBookmarkChallengeItemSerializer
        # Default case for unhandled methods
        return BookmarkChallengeItemSerializer


    def get_queryset(self):
        return models.BookmarkChallengeItem.objects.\
    filter(container=self.kwargs['bookmark_pk']).\
    select_related('challenge')

    def perform_create(self, serializer):
    # Directly use bookmark_pk to set the container field
        bookmark_pk = self.kwargs.get('bookmark_pk')

        # Optionally validate if the BookmarkChallengeContainer exists
        try:
            container_instance = models.BookmarkChallengeContainer.objects.get(id=bookmark_pk)
        except models.BookmarkChallengeContainer.DoesNotExist:
            raise ValidationError({"container": "The specified container does not exist."})

        # Save the new BookmarkChallengeItem, associating the container with the provided bookmark_pk
        serializer.save(container=container_instance)


class OrderingFeedBackViewSet(ModelViewSet):
    # serializer_class = OrderingFeedBackSerializer
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get','post','patch','delete','head','options']
    def get_permissions(self):
        if self.request.method in ['PATCH','DELETE']:
         return [IsAdminUser()] 
        return [IsAuthenticated()]


    def create(self, request, *args, **kwargs):
        serializer = CreateOrderingFeedBackSerializer(
        data=request.data,
        context ={ 'user_id':self.request.user.id})
        serializer.is_valid(raise_exception=True)
        models.OrderingFeedBack = serializer.save()
        serializer = OrderingFeedBackSerializer(models.OrderingFeedBack)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderingFeedBackSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderingFeedBackSerializer
        return OrderingFeedBackSerializer

    # def get_serializer_context(self):
    #     return {'user_id':self.request.user.id}

    def get_queryset(self):
        user = self.request.user
        try:
            if user.is_staff and user.is_superuser:
                return models.OrderingFeedBack.objects.all()
            student = models.Student.objects.only('user').get(user=user)
        except models.Student.DoesNotExist:
            raise ValidationError({"detail": "No associated student record found for the current user."})
        
        return models.OrderingFeedBack.objects.filter(student_id=student)
    
    










    
