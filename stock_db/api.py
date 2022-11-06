from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

class DatasetList(APIView):
    def get(set, request):
        datas = Dataset.objects.all()
        serializer = DatasetSerializer(datas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatasetDetail(APIView):
    def get(selt, request, dataset_id):
        datas = Dataset.objects.get(id=dataset_id)
        serializer = DatasetSerializer(datas)
        return Response(serializer.data)

    def put(self, request, dataset_id):
        datas = Dataset.objects.get(id=dataset_id)

        serializer = DatasetSerializer(datas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, dataset_id):
        datas = Dataset.objects.get(id=dataset_id)
        datas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)