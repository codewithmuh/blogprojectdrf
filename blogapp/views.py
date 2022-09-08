# This is importing all the necessary libraries and modules for the project.
from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q
from django.core.paginator import Paginator

# This class is used to fetch all the blogs from the database

class PublicBlogView(APIView):
    def get(self, request):
        try:
            blogs = Blog.objects.all()
            
            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))
                
            page_number = request.GET.get('page', 1)
            paginator = Paginator(blogs, 5)     
            
            serializer = BlogSerializer(paginator.page(page_number), many =True)
        
            return Response({
                  'data': serializer.data,
                  'message': 'Blogs data fetched successfully'
            }, status= status.HTTP_200_OK)
            
        except Exception as e:
             print(e)
             return Response({
                   'data' : {},
                   'message' : 'something went wrong in data access'
                }, status= status.HTTP_400_BAD_REQUEST) 
     
    

# This class is used to create, update, delete and list blogs

class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[JWTAuthentication]
    
    def get(self, request):
        try:
            blogs = Blog.objects.filter(user=request.user)
            
            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))
                
            page_number = request.GET.get('page', 1)
            paginator = Paginator(blogs, 5)     
            
            serializer = BlogSerializer(paginator.page(page_number), many =True)
        
            return Response({
                  'data': serializer.data,
                  'message': 'Blogs data fetched successfully'
            }, status= status.HTTP_200_OK)
            
        except Exception as e:
             print(e)
             return Response({
                   'data' : {},
                   'message' : 'something went wrong in data access'
                }, status= status.HTTP_400_BAD_REQUEST) 
             
     
    def post(self, request):
        try:
            data  = request.data
            data['user'] = request.user.id
            serializer = BlogSerializer(data =data)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status= status.HTTP_500_BAD_REQUEST)
                
            serializer.save()    
            
            return Response({
                'data': serializer.data,
                'message': 'Blog created successfully'
            }, status= status.HTTP_201_CREATED)
        
            
        except Exception as e:
             print(e)
             return Response({
                   'data' : {},
                   'message' : 'something went wrong in data access yyyy'
                }, status= status.HTTP_400_BAD_REQUEST)       
                
        
    def patch(self, request ):
        try:
            data = request.data
            blog = Blog.objects.filter(uid= data.get('uid'))   
            
            if request.user != blog[0].user:
                return Response({
                    'data': {},
                    'message': "You are not authorized to update this blog"
                }, status= status.HTTP_401_UNAUTHORIZED) 
                
                
            if not blog.exists():
                
                return Response({
                    'data': {},
                    'message': 'Blog not found with this uid'   
                }, status = status.HTTP_404_NOT_FOUND)
                
            serializer = BlogSerializer(blog[0],  data = data, partial = True)  
            
                
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status= status.HTTP_500_BAD_REQUEST)
                
            serializer.save()    
            
            return Response({
                'data': serializer.data,
                'message': 'Blog updated successfully'
            }, status= status.HTTP_200_OK)
        
            
        except Exception as e:
             print(e)
             return Response({
                   'data' : {},
                   'message' : 'something went wrong in data access'
                }, status= status.HTTP_400_BAD_REQUEST) 
            
              

    def delete(self, request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid= data.get('uid'))  
            
            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'Blog not found with this uid'   
                }, status = status.HTTP_400_BAD_REQUEST) 
            
            if request.user != blog[0].user:
                return Response({
                    'data': {},
                    'message': "You are not authorized to update this blog"
                }, status= status.HTTP_401_UNAUTHORIZED) 
                
                
            blog[0].delete()
            
            return Response({
                  'data': {},
                  'message': 'Blog deleted successfully'
            }, status= status.HTTP_200_OK)
             
        except Exception as e:
             print(e)
             return Response({
                   'data' : {},
                   'message' : 'something went wrong in data access'
                }, status= status.HTTP_400_BAD_REQUEST)   
        
            
            