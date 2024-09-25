from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .parsers.csv_parser import parse_csv
from .parsers.json_parser import parse_json
from .services.client_processor import ClientProcessor
import os
import csv

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def process_file(request):
    source_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'))

    csv_data = parse_csv(os.path.join(source_folder, 'data.csv'))
    json_data = parse_json(os.path.join(source_folder, 'data.json'))["results"]

    response = []
    processor = ClientProcessor()

    for data in json_data:
        response.append(processor.process(data))

    for data in csv_data:
        response.append(processor.process(data))

    paginator = CustomPagination()
    paginated_response = paginator.paginate_queryset(response, request)
        
    try:
        return paginator.get_paginated_response(paginated_response)
    except Exception as e:
        return Response({'error': str(e)}, status=500)