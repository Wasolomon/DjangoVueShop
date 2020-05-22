from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3  # 每页显示多少个数据
    page_size_query_param = 'size'  # 默认每页显示3页
    max_page_size = 10  # 最大页数不超过10页
    page_query_param = 'page'  # 获取页码数值

