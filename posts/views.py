from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated]
  queryset = Post.objects.all()
  
  def get(self, request:Request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def post(self, request:Request, *args, **kwargs):
    return self.create(request, *args, **kwargs)




class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
  serializer_class = PostSerializer
  queryset = Post.objects.all()
  
  def get(self, request:Request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  def put(self, request:Request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  
  def delete(self, request:Request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  
  












#CLASS BASE API VIEWS

# class PostListCreateView(APIView):
#   serializer_class = PostSerializer
  
#   # def get(self, request:Request, *args, **kwargs):
#   #   posts = Post.objects.all()
    
#   #   serializer = self.serializer_class(instance=posts, many=True)
    
#   #   return Response(data=serializer.data, status=status.HTTP_200_OK)
  
#   # def post(self, request:Request, *args, **kwargs ):
#   #   data = request.data
    
#   #   serializer = self.serializer_class(data=data)
    
#   #   if serializer.is_valid():
#   #     serializer.save()
      
#   #     response = {
#   #       "Message": "Post created successfully",
#   #       "data": serializer.data
#   #     }
      
#   #     return Response(data=response, status=status.HTTP_201_CREATED)
    
#   #   return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class PostRetrieveUpdateDeleteView(APIView):
#   serializer_class = PostSerializer
  
   # def get(self, request:Request, pk:int):
#   #   post = Post.objects.get(pk=pk)
    
#   #   serializer = self.serializer_class(post)
    
#   #   if serializer:
      
#   #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#   #   return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
  
#   # def put(self, request:Request, pk=None):
#   #   post = get_object_or_404(Post, pk=pk)
    
#   #   data = request.data
    
#   #   serializer = self.serializer_class(instance=post, data=data)
    
#   #   if serializer.is_valid():
#   #     serializer.save()
      
#   #     response = {
#   #       "message": "Post update successfully",
#   #       "data": serializer.data
#   #     }
      
#   #     return Response(data=response, status=status.HTTP_200_OK)
    
#   #   return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   # def delete(self, request:Request, pk: int):
#   #   post = get_object_or_404(Post, pk=pk)
    
#   #   post.delete()
    
#   #   return Response(status=status.HTTP_204_NO_CONTENT)
  
  




# class PostViewset(viewsets.ViewSet):
#   def list(self, request:Request):
#     queryset = Post.objects.all()
    
#     serializer = PostSerializer(instance=queryset, many=True)
    
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  
#   def retrieve(self, request:Request, pk=None):
#     post = get_object_or_404(Post, pk=pk)
    
#     serializer = PostSerializer(instance=post)
    
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  
#   def create(self, request:Request):
#     data = request.data
    
#     serializer = PostSerializer(Post, data=data)
    
#     if serializer.is_valid():
#       serializer.save()
      
#       response = {
#         "Message": "post created successfully",
#         "data": serializer.data
#       }
      
#       return Response(data=response, status=status.HTTP_201_CREATED)
    
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Funtion based API View

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):
  
#   if request.method == "POST":
#     data = request.data
    
#     response = {"Message": "Hello, world!", "data": data}
    
#     return Response(data=response, status=status.HTTP_201_CREATED)
  
#   response = {"Message": "hello world"}
#   return Response(data=response, status=status.HTTP_200_OK)

#write me a view to create post or list post depending on the HTTP method
# #
# @api_view(http_method_names=["GET", "POST"])
# def list_posts(request:Request):
#   posts = Post.objects.all()
  
#   if request.method == "POST":
#     data = request.data
    
#     serializer = PostSerializer(data=data)
    
#     if serializer.is_valid():
#       serializer.save()
      
#       response = {
#         "Message": "Post saved successfully",
#         "data": serializer.data
#       }
      
#       return Response(data=response, status=status.HTTP_201_CREATED)
    
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   serializer = PostSerializer(instance=posts, many=True)
  
#   response = {"Message": "Message", "data": serializer.data}
  
#   return Response(data=response, status=status.HTTP_200_OK)


# #Post Detail View
# @api_view(http_method_names=["GET"])
# def post_detail(request:Request, pk=None):
#   post = get_object_or_404(Post, pk=pk)
  
#   serializer = PostSerializer(instance=post)
  
#   if post:
    
#     response = {
#       "message": "Post detail",
#       "data": serializer.data
#     }
    
#     return Response(data=response, status=status.HTTP_200_OK)
  
#   return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)



# # Update View
# @api_view(http_method_names=["PUT"])
# def update_post(request:Request, pk=None):
#   post = get_object_or_404(Post, pk=pk)
  
#   data = request.data
  
#   serializer = PostSerializer(instance=post, data=data)
  
#   if serializer.is_valid():
#     serializer.save()
    
#     response = {
#       "message": "Post updated successfully",
#       "data": serializer.data
#     }
    
#     return Response(data=response, status=status.HTTP_200_OK)
  
#   return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Delete view
# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request, pk=None):
  # post = get_object_or_404(Post, pk=pk)
  
  # post.delete()
  
  # return Response(status=status.HTTP_204_NO_CONTENT)