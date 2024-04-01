from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo_list.models import Todo
from todo_list.serializers import TodoSerializer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.exceptions import PermissionDenied


class TodoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        todo = serializer.save(user=self.request.user)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(self.request.user.id),
            {
                "type": "todo_message",
                "message": {
                    "action": "create",
                    "object_type": "todo",
                    "data": {
                        "id": str(todo.id),
                        "title": todo.title,
                        "description": todo.description,
                        "completed": todo.completed,
                    },
                },
            },
        )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied()
        todo = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(self.request.user.id),
            {
                "type": "todo_message",
                "message": {
                    "type": "todo_message",
                    "message": {
                        "action": "update",
                        "object_type": "todo",
                        "data": {
                            "id": str(todo.id),
                            "title": todo.title,
                            "description": todo.description,
                            "completed": todo.completed,
                        },
                    },
                },
            },
        )

    def perform_destroy(self, instance):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied()
        todo_id = instance.id
        instance.delete()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(self.request.user.id),
            {
                "type": "todo_message",
                "message": {
                    "type": "todo_message",
                    "message": {
                        "action": "delete",
                        "object_type": "todo",
                        "data": {
                            "id": str(todo.id),
                        },
                    },
                },
            },
        )

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
