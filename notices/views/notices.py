from django.http import JsonResponse
from ..models import Notice
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated]) 
def listAllNotices(request):
    output = {}
    # No database activity actually occurs until
    # we do something to evaluate the queryset.
    # list() forces evaluation of a QuerySet
    output["list"] = list(Notice.objects.values())
    return JsonResponse(output)


