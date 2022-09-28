SEARCH_KEY = 'q'


def search_text_filter(**kwargs):
    model = kwargs['model']
    queryset = kwargs['queryset']
    request = kwargs['request']

    keyword = request.query_params[SEARCH_KEY]

    if SEARCH_KEY in request.query_params:
        return queryset.filter(model.name.ilike('%' + keyword + '%'))

    return queryset
