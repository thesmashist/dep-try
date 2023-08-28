from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        'api/token/verify',
        'api/member',
        'api/member/<int:id>',
        'api/login/<int:id>',
        'fmp/<int:id>/stats',
        'fmp/<str:region>/season/<department>',
        'bb/bbt/',
    ]

    return Response(routes)