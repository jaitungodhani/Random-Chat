from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.


@permission_classes([AllowAny])
def testing(request):
    return render(request, 'test.html')