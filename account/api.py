from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('is_superuser',)
    search_fields = ('username', 'email')
    ordering_fields = ('username', 'email')
    ordering = ('username',)

    '''
    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.pk)
    '''

    def get_object(self):
        pk = self.kwargs['pk']
        if pk == 'me':
            return self.request.user
        else:
            return super().get_object()
