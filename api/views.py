from rest_framework.decorators import api_view
from rest_framework.response import Response
from .web_crawler import main
from rest_framework import status


@api_view(['GET'])
def product_list(request, word=None, format=None):
    if request.method == 'GET':
        main.web_scrapping(word)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
