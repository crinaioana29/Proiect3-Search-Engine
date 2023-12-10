import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.decorators import api_view
from .web_crawler import main


@api_view(['GET'])
def product_list_template(request, word=None):
    if request.method == 'GET':
        df = main.web_scraping(word)
        json_data = json.dumps(df, ensure_ascii=False, default=str, indent=None)
        json_new_data = json.loads(json_data)
        template = loader.get_template("api/../templates/home.html")
        # Render the HTML template with JSON data
        return HttpResponse(template.render({'json_data': json_new_data}, request))


def index(request):
    return render(request, 'api/../templates/index.html')
