from models import TodoTable
from rest_framework import viewsets,permissions
from serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset=TodoTable.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=TodoSerializer