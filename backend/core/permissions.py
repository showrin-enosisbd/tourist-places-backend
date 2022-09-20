from rest_framework.permissions import SAFE_METHODS


def has_permission_for_item(request, item):
    if request.method in SAFE_METHODS:
        return True

    else:
        return item.creator == request.user
