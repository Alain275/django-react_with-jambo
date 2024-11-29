# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# we use this if we want to list only the data
# there is update , delete or create data
# from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models
from .serializers import  ChallengeSerializer,ReviewSerializer

@api_view()
def hero_world_view(request):
    # queryset = User.objects.filter(id__range=(7, 20)).order_by('-id')  # Adjust the range as needed
    # context = {
    #     'users': queryset  # Passing the queryset to the template
    # }
    # return render(request, 'index.html', context)

    return Response("okay")

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
    serializer_class = ChallengeSerializer

class ReviewViewSet(ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = ReviewSerializer





    
