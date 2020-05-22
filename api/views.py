from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer
from utils.handle_message import menu_data


# class SnippetViewSet(viewsets.ModelViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

#
# def menu_index(request):
#     return JsonResponse(menu_data)
