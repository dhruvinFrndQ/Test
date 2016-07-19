from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def call_api(request):
    """
    """
    dict = {'Message': 'ERROR'}
    if request.method == 'POST':
        data=request.data
        if data['service'] == "conference":
              dest=data['destination']
              print("conference user ", dest)
              return Response(request.data,status=status.HTTP_200_OK)
        elif data['service'] == "play":
              dest=data['destination']
              print("play annoucment to user ", dest)
              return Response(request.data,status=status.HTTP_200_OK)        
        return Response(dict,status=status.HTTP_200_OK)
