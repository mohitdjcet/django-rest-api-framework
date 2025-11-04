from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        return Response({"message": "Public can view this data"})
    elif request.method == 'POST':
        return Response({"message": f"Data created by {request.user.username}"})