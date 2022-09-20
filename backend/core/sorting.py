SORT_DIRECTION_KEY = 'sort_direction'
SORT_BY_KEY = 'sort_by'
SORT_DIRECTION_ASC = 'asc'
SORT_DIRECTION_DESC = 'desc'


def get_sorted_data(**kwargs):
    queryset = kwargs['queryset']
    request = kwargs['request']

    direction = request.query_params[SORT_DIRECTION_KEY] if SORT_DIRECTION_KEY in request.query_params else None
    sort_field = request.query_params[SORT_BY_KEY] if SORT_BY_KEY in request.query_params else None

    if sort_field and direction:
        if direction == SORT_DIRECTION_ASC:
            queryset = queryset.order_by(sort_field)
        elif direction == SORT_DIRECTION_DESC:
            sort_field = '-' + sort_field
            queryset = queryset.order_by(sort_field)
        else:
            queryset = queryset

    return queryset
