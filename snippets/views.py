from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

# The root of our API is going to be a view that
# supports listing all the existing snippets, or
# creating a new snippet.

# To POST to this view from clients that won't have a
# CSRF token we need to mark the view as csrf_exempt.
# @csrf_exempt
# def snippet_list(request):
#   """
#   List all code snippets, or create a new snippet.
#   """
#   if request.method == 'GET':
#     snippets = Snippet.objects.all()
#     serializer = SnippetSerializer(snippets, many=True)
#     return JsonResponse(serializer.data, safe=False)

#   elif request.method == 'POST':
#     data = JSONParser().parse(request)
#     serializer = SnippetSerializer(data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

# REST framework provides two wrappers you can use to write API views:
  # The @api_view decorator for working with function based views.
  # The APIView class for working with class-based views.
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def snippet_list(request, format=None):
  """
  List all code snippets, or create a new snippet.
  """
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = SnippetSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# One of the big wins of using class-based views is
# that it allows us to easily compose reusable bits
# of behaviour.
class SnippetList(APIView):
  """
  List all snippets, or create a new snippet.
  """
  def get(self, request, format=None):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = SnippetSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Building the view using GenericAPIView, and
# add in ListModelMixin and CreateModelMixin.
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

# @csrf_exempt
# def snippet_detail(request, pk):
#   """
#   Retrieve, update or delete a code snippet.
#   """
#   try:
#     snippet = Snippet.objects.get(pk=pk)
#   except Snippet.DoesNotExist:
#     return HttpResponse(status=404)

#   if request.method == 'GET':
#     # Read
#     serializer = SnippetSerializer(snippet)
#     return JsonResponse(serializer.data)

#   elif request.method == 'PUT':
#     # Update
#     data = JSONParser().parse(request)
#     serializer = SnippetSerializer(snippet, data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return JsonResponse(serializer.data)
#     return JsonResponse(serializer.errors, status=400)

#   elif request.method == 'DELETE':
#     # Delete
#     snippet.delete()
#     return HttpResponse(status=204)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
  """
  Retrieve, update or delete a code snippet.
  """
  try:
    snippet = Snippet.objects.get(pk=pk)
  except Snippet.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = SnippetSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Use the GenericAPIView class to provide the core
# functionality, and adding in mixins to provide the
# .retrieve(), .update() and .destroy() actions.
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


class SnippetList(generics.ListCreateAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  # By overriding a .perform_create() method on the snippet
  # views, that allows us to modify how the instance save
  # is managed, and handle any information that is implicit
  # in the incoming request or requested URL.
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer