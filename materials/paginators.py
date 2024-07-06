from rest_framework.pagination import PageNumberPagination


class MaterialsPagination(PageNumberPagination):
    """ Настройка пагинации для курсов и уроков """
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10
