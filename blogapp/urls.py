from django.urls import path, include


from blogapp.views import  BlogView


urlpatterns = [
    path('blogs/', BlogView.as_view() , name='blogs'),
  
]



