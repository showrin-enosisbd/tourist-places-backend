from urllib import request
from rest_framework.pagination import PageNumberPagination


def get_paginted_result(**kwargs):
    queryset = kwargs['queryset']
    request = kwargs['request']
    page_size = kwargs['page_size']
    Seriazer_Clase = kwargs['serializer']

    paginator = PageNumberPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = Seriazer_Clase(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
