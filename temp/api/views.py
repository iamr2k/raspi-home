# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import temp_log
import requests
from .serializers import tempSerializer
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
def check():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        url = "http://raspberrypi.local/api/"
        data = {
            "temp":temperature,
            "humidity":humidity
        }
        # requests.post(url, data=data)
    else:
        temperature = 0
        humidity = 0
    resp = {"temperature":round(temperature,1),"humidity":round(humidity,2)}
    return resp


# class tempViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint .
#     """

    
#     # k = check()
#     queryset = temp_log.objects.all().order_by('-time')

#     serializer_class = tempSerializer


class tempViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = tempSerializer
    def get(self,request):
        k = check()
        # queryset = temp_log.objects.all().order_by('-id')
        # serializer = self.serializer_class(queryset, many=True)
        
        # return Response(data=serializer.data)
        return Response(data=k)

    # def post(self, request):
    #     ser = self.serializer_class(
    #         data=request.data,
    #         context={'request': request}
    #     )
    #     if ser.is_valid():
    #         ser.save()
    #     return Response(data={"status":"ok"})