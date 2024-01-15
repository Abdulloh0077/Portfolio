from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MyAPIView(APIView):
    def get(self, request, format=JSON):
        data = {'message': 'GET so\'rovi qabul qilindi'}
        return Response(data, status=status.HTTP_200_OK)