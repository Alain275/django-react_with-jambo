from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, DjangoModelPermissions
from rest_framework.decorators import action
from main.permissions import ViewCustomerHistory
from rest_framework import status
from . import models
from .serializers import StudentSerializer

# Custom permission for authenticated users to manage only their own profile
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin users can perform any action
        if request.user.is_staff:
            return True
        # Regular users can update only their own profile
        return obj.user == request.user

class StudentViewSet(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]  # Ensure Django model permissions are applied

    def get_permissions(self):
        # Get the default set of permissions
        permissions = super().get_permissions()

        if self.action in ['list', 'retrieve']:
            # Allow all authenticated users to view students
            permissions = [IsAuthenticated()] + permissions

        if self.action == 'me':
            # Allow authenticated users to view or update their own profile
            permissions = [IsAuthenticated()] + permissions

        if self.request.method == 'POST' or self.request.method == 'DELETE':
            # Restrict creation and deletion to admin users only
            permissions = [IsAdminUser()] + permissions

        if self.request.method == 'PUT':
            # Restrict updates based on ownership
            permissions = [IsOwnerOrAdmin()] + permissions

        # Return combined permissions
        return permissions
    
    @action(detail=True,permission_classes=[ViewCustomerHistory])
    def history(self,request,pk):
        return Response("ok")

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        # Retrieve or update the authenticated user's profile
        try:
            student = models.Student.objects.get(user=request.user)
        except models.Student.DoesNotExist:
            return Response(
                {"detail": "Student profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        if request.method == 'GET':
            serializer = self.get_serializer(student)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = self.get_serializer(student, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
