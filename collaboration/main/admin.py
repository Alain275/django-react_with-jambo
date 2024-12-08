from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from user.models import User,Student,intake
from .models import Challenges,Review,BookmarkChallengeItem,BookmarkChallengeContainer,OrderingFeedBack,OrderingFeedBackItem
from django.utils.html import mark_safe

from django.contrib import admin

# admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(intake)
# admin.site.register(Challenges)
admin.site.register(OrderingFeedBackItem)
admin.site.register(OrderingFeedBack)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Display fields in list view

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name",),  # Add fields for the add form
            },
        ),
    )



@admin.register(BookmarkChallengeContainer)
class ChallengeAdmin(admin.ModelAdmin):
   
   # List the fields to display in the admin list view
    list_display = [ id,'get_user_first_name']
    list_filter = ['created_at']
    list_per_page = 3  # Pagination: 3 items per page

    # Method to get the user's first name
    def get_user_first_name(self, obj):
        return obj.user.first_name
    get_user_first_name.short_description = 'bookmark challenges owner'

@admin.register(BookmarkChallengeItem)
class ChallengeAdmin(admin.ModelAdmin):
   
   # List the fields to display in the admin list view
    list_display = [ 'challenge_name']
    list_filter = ['created_at']
    list_per_page = 3  # Pagination: 3 items per page

    # Method to get the user's bookmark
    def bookmark_name(self, obj):
        return obj.container.crested_at
    bookmark_name.short_description = 'bookmark date of creation'

    # Method to get the user's challenge
    def challenge_name(self, obj):
        return obj.challenge.challenge_name
    challenge_name.short_description = 'challenge name'



@admin.register(Review)
class ChallengeAdmin(admin.ModelAdmin):
   
   # List the fields to display in the admin list view
    list_display = ['get_user_first_name', 'rating_stars']
    list_filter = ['created_at']
    list_per_page = 3  # Pagination: 3 items per page

    # Method to get the user's first name
    def get_user_first_name(self, obj):
        return obj.user.first_name
    get_user_first_name.short_description = 'User First Name'

    # Method to display stars based on the rating
    def rating_stars(self, obj):
        return mark_safe('★' * obj.rating)  # Assuming rating is an integer between 1 and 5
    rating_stars.short_description = 'Rating '




@admin.register(Challenges)
class ChallengeAdmin(admin.ModelAdmin):
    actions = ['clear_comments']  # List of actions
    list_display = ['challenge_name', 'date_creation']
    list_filter = ['date_creation']
    list_per_page = 3  # Pagination: 3 items per page

    @admin.action(description='Clear comments')
    def clear_comments(self, request, queryset):
        # Clear the comments field for selected items
        updated_comments = queryset.update(comment='no coments!')
        self.message_user(
            request,
            f"{updated_comments} comment{'s' if updated_comments != 1 else ''} have been updated."
        )



# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
  
#     list_display = ['full_name', 'year_of_study','IC_CS']
#     list_filter = ['year_of_study']
#     list_editable = ['year_of_study']  
#     search_fields = ['first_name__istartswith','last_name__istartswith']
#     list_per_page = 3  

#     def IC_CS(self,obj):
#         if obj.year_of_study==User.YEAR_1 or obj.year_of_study==User.YEAR_2:
#          return 'COMPUTER SCIENCE '
#         else :
#          return 'INFORMATION SYSTEM'
        
#     IC_CS.short_description = 'Program(CS & IS)'

      


@admin.register(Student)
class User_profileAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['username','first_name','last_name','full_name', 'Bio','year_of_study','IC_CS']
    list_filter = ['user__first_name']
   
    # list_editable = ['challenge_name']  
    list_per_page = 3
    list_select_related = ['user']

    def IC_CS(self,obj):
        if obj.year_of_study==Student.YEAR_1 or obj.year_of_study==Student.YEAR_2:
            return 'COMPUTER SCIENCE '
        else :
            return 'INFORMATION SYSTEM'
        
    IC_CS.short_description = 'Program(CS & IS)'

# @admin.register(intake)
# class intakeAdmin(admin.ModelAdmin):
#     list_display = ['user__first_name','intake_id']
#     list_filter = ['intake_id']

    
   
#     # list_editable = ['challenge_name']  
#     list_per_page = 3


# class IntakeInline(admin.TabularInline):
#     model = User
@admin.register(intake)
class IntakeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    search_fields = ['user__first_name__istartswith','user__last_name__istartswith']
    # inlines = [IntakeInline]
    list_display = ['user_first_name', 'intake_ordinal']  # Replace with your actual fields
    # list_filter = ['user__first_name']  # You can filter by related field
    list_per_page = 3

    def user_first_name(self, obj):
        return obj.user.first_name  # Assuming 'user' is the related field pointing to the User model
    user_first_name.short_description = 'User First Name'

    def intake_ordinal(self, obj):
        return intake.ordinal(obj.intake_id)  # Call the static method
    intake_ordinal.short_description = 'intake ID'  # Set column name

    
    



