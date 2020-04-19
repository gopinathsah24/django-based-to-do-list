from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Task
from tasks.api.serializers import TaskSerializers

@api_view(['GET',])
def api_detail_task_view(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=TaskSerializers(task)
        return Response(serializer.data)
@api_view(['PUT',])
def api_update_task_view(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
       
    if request.method =='PUT':
        serializer= TaskSerializers(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'success':'update successful'}
            return Response(data=data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'],)
def api_delete_view(request,pk):
    try:
        item = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    
    if request.method=="DELETE":
        operation = item.delete()
        data = {}
        if operation:
            data["delete"]="delete successfull"
        else: 
            data["delete"]="delete unsuccessfull"
        return Response(data=data)


@api_view(['POST',])
def api_create_view(request):

       
    if request.method =='POST':
        serializer= TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'success':'post created '}
            return Response(data=data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)