from rest_framework import generics, response, status
from profits import models, serializers, permissions


class TradeViewSet(generics.CreateAPIView, generics.ListAPIView):
    print("viewset")
    # permission_classes = (permissions.Check_API_KEY_Auth,)
    queryset = models.Trade.objects.all()
    serializer_class = serializers.TradeSerializer

    def create(self, request, *args, **kwargs):
        # self.user = request.user
        trades = request.data["trades"]
        serializer = self.get_serializer(data=trades, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return response.Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
