from rest_framework import viewsets, mixins, response,status
from profits import models, serializers


class TradeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  queryset = models.Trade.objects.all()
  serializer_class = serializers.TradeSerializer

  def create(self, request, *args, **kwargs):
    # self.user = request.user 
    trades = request.DATA['trades']
    serializer = self.get_serializer(data=trades, files=request.FILES, many=True):
    if serializer.is_valid():
      serializer.save()
      headers = self.get_success_headers(serializer.data)
      return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)