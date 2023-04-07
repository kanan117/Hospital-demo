

from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ContactSerializer
from core.models import Contact


class ContactViewSet(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        Contact = Contact.objects.all()
        serializer = ContactSerializer(Contact, many=True)
        return Response(serializer.data)
    

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class ContactDetailViewSet(APIView):
    
    def get(self, request, id, *args, **kwargs):
        Contact_detail = Contact.objects.get(id=id)
        serializer = ContactSerializer(Contact_detail, many=False)
        return Response(serializer.data)
    
    def put(self, request, id, *args, **kwargs):
        Contact_detail = Contact.objects.get(id=id)
        serializer = ContactSerializer(instance=Contact_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id, *args, **kwargs):
        Contact = Contact.objects.filter(id=id).first()
        Contact.delete()
        return Response('deleted')
    