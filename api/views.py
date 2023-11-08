import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .web_crawler import main
from rest_framework import status


def product_list_api(request, word=None, format=None):
    if request.method == 'GET':
        df = main.web_scrapping(word)
        json_data = json.dumps(df, ensure_ascii=False, default=str, indent=None)
        json_new_data = json.loads(json_data)
        return Response(json_new_data, content_type='application/json', status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def product_list_template(request, word=None):
    if request.method == 'GET':
        df = main.web_scrapping(word)
        json_data = json.dumps(df, ensure_ascii=False, default=str, indent=None)
        json_new_data = json.loads(json_data)
        template = loader.get_template("api/../templates/home.html")
        # Render the HTML template with JSON data
        return HttpResponse(template.render({'json_data': json_new_data}, request))


def index(request):
    return render(request,'api/../templates/index.html')