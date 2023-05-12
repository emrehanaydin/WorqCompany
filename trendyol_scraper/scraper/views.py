from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RequestSerializer
from .helpers import is_true_url, ProductSaveHelpers

helpers = ProductSaveHelpers()


class ProductAPIView(APIView):

    def post(self, request):
        serializer = RequestSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        url = serializer.data['url']

        if not is_true_url(url):
            return Response("Wrong URL ", status=status.HTTP_406_NOT_ACCEPTABLE)

        return helpers.save_product_details(url=url)
