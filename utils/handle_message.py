from django.core.cache import cache
from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import set_rollback
from rest_framework.viewsets import ModelViewSet


# class ReturnMessage:
#     def __init__(self, code=200, message='success', errors=None, data=None):
#         self.code = code
#         self.message = message
#         self.errors = {} if errors is None else errors
#         self.data = [] if data is None else data
#
#     def message(self):
#         return {
#             'code': self.code,
#             'message': self.message,
#             'errors': self.errors,
#             'data': self.data
#         }


class MessageViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'code': 200, 'message': 'success', 'errors': {}, 'data': response.data},
                        status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({'code': 200, 'message': 'success', 'errors': {}, 'data': response.data},
                        status=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'code': 200, 'message': 'success', 'errors': {}, 'data': response.data},
                        status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'code': 200, 'message': 'success', 'errors': {}, 'data': []},
                        status=response.status_code)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({'code': 200, 'message': 'success', 'errors': {}, 'data': response.data},
                        status=response.status_code)


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            if isinstance(exc.detail, list):
                errors = exc.detail
            else:
                errors = {k: v[0] for k, v in exc.detail.items()}
        else:
            errors = exc.detail

        set_rollback()
        return Response({'code': 0, 'message': 'failure', 'errors': errors, 'data': []}, status=exc.status_code,
                        headers=headers)

    return None


def response_format(code, data=None, token=None):
    res = {
        "meta": {
            'success': True if code == 200 else False,
            'status': code,
            'message': custom_message[code]
        },
        "data": data
    }
    if token:
        res.update({'token': cache.get('token')})
    return res


custom_message = {
    200: '请求服务器成功',
    100101: '请填写所有的参数',
    100102: '两次输入的密码不一样',
    100103: '输入的字段格式不正确',
    100104: '用户名或手机号在数据库已经存在',
    100105: '用户名或密码错误',
}
