from rest_framework import  filters , status ,viewsets
from .models import  Artist, Work,Client
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer , UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
from django.template import loader

def home_view(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
    

class WorkListView(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['work_type']

    def get_queryset(self):
        queryset = super().get_queryset()
        artist_name = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)
        if artist_name is not None:
            queryset = queryset.filter(artist__name=artist_name)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        return queryset
   

class ArtistListView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']




class UserRegistration(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            client = Client.objects.get(user=user)
            client_serializer = ClientSerializer(client)
            return Response({'user': serializer.data, 'client': client_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



