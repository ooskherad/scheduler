from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def test(request):
    data = request.data
    info = UserSerializer(data=data)
    if info.is_valid():
        info.create(validated_data=info)
    else:
        print(info.errors)
    return Response({'data': data})
