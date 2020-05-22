from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Right, Role, Menu, Category
from .serializers import UserSerializers, RightSerializer, RoleSerializer, MenuSerializer, CategorySerializer, CategoryLevelSerializer
from utils.page_size import MyPageNumberPagination
from utils.handle_message import response_format, MessageViewSet
from utils.check_field import check_mobile, check_password, check_username
from utils.token_certification import token
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserViewSet(MessageViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = MyPageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('username',)

    # step1: user register
    @action(methods=["POST"], detail=False, url_name='register', url_path='register')
    def register(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        mobile = request.data.get('mobile')

        if not (username and password and mobile):
            return Response(response_format(100101))

        if not (check_username(username) and check_password(password) and check_mobile(mobile)):
            return Response(response_format(100103))

        if User.objects.filter(Q(username=username) | Q(mobile=mobile)):
            return Response(response_format(100104))

        User(username=username, password=password, mobile=mobile).save()
        return Response(response_format(200))

    # step2: user login
    @action(methods=["POST"], detail=False, url_name='login', url_path='login')
    def login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # todo: user input mobile to login
        if not (username or password):
            return Response(response_format(100101))

        if not (check_username(username) and check_password(password)):
            return Response(response_format(100103))

        user_object = User.objects.filter(Q(username=username), Q(password=password))
        if user_object:
            cache.set('token', token)
            # 对请求接收到的字段进行序列化
            serializer_context = {
                'request': request,
            }
            data = UserSerializers(user_object, context=serializer_context, many=True).data[0]
            return Response(response_format(200, data, token=True))

        return Response(response_format(100105))


class RightViewSet(MessageViewSet):
    queryset = Right.objects.all()
    serializer_class = RightSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('level',)


class RoleViewSet(MessageViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class MenuViewSet(MessageViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CategoryViewSet(MessageViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('level',)


class CategoryLevelView(MessageViewSet):
    queryset = Category.objects.filter(level='2')
    serializer_class = CategoryLevelSerializer
