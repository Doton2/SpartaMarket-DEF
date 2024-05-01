from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from rest_framework import status, viewsets
from .models import Product
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ProductAPIView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author_id=request.user.id)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        
    def get(self, request):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        res_pag = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(res_pag, many=True)
        return paginator.get_paginated_response(serializer.data)
    

class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, product_id):
        product = get_object_or_404(Product,id=product_id)
        if product.author_id == request.user.id:
            serializer = ProductSerializer(product,data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        message = {'message': f'author{product.author_id} is different '}  
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, product_id):
        product = get_object_or_404(Product,id=product_id)
        if product.author_id == request.user.id:
            product.delete()
            message = { 'message': f'product{product_id} delete'}
            return Response(message,status=status.HTTP_200_OK)
        message = {'message': f'author{product.author_id} is different'}  
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    