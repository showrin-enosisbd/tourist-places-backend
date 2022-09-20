SEARCH_KEY = 'q'


def search_text_filter(**kwargs):
    queryset = kwargs['queryset']
    request = kwargs['request']

    if SEARCH_KEY in request.query_params:
        return queryset.filter(name__icontains=request.query_params[SEARCH_KEY])

    return queryset
