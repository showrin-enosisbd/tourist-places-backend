import math
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        item_count_per_page = self.page_size
        total_items = self.page.paginator.count

        return Response({
            'total_pages': math.ceil(total_items/item_count_per_page),
            'count': self.page.paginator.count,
            'results': data
        })


def get_paginted_result(**kwargs):
    queryset = kwargs['queryset']
    request = kwargs['request']
    page_size = kwargs['page_size']
    Serializer_Class = kwargs['serializer']

    paginator = CustomPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = Serializer_Class(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
