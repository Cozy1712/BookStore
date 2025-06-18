from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel
from rest_framework import serializers


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'

    def validate(self,data):
        price = data['price']
        if price < 0:
            raise serializers.ValidationError(f'price cannot be Negative')
        return data
        
@api_view(['GET'])
def BookListApi(request):
    #Fetch from Database
    books = BookModel.objects.all()
   # cconvert to json using serializer
    serializer = BookModelSerializer(books,many=True)

    # Send Response
    return Response(serializer.data)

@api_view(['POST'])
def BookCreateApi(request):
    # Get Data from request
    data = request.data

    serializer = BookModelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
        'Message': 'Book Created Successfully',
        })
 
    return Response(serializer.errors)

    
   
@api_view(['PUT'])
def BookUpdateApi(request, id):
    # Get data from request
    data = request.data

    book = BookModel.objects.get(id=id)

    serializer = BookModelSerializer(instance = book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({ 
            'Message': 'Book Updated Successfully'
        })
    return Response(serializer.errors)

@api_view(['DELETE'])
def BookDeleteApi(request, id):
    # Get .book from database
    book = BookModel.objects.get(id=id)
    book.delete()
    return Response({
        'Message': 'Book Deleted Successfully'
    })