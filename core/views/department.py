
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.serializers import DepartmentSerializer


@api_view(['POST'])
def department_create(request):
    serializer = DepartmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
