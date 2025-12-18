from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

# Class-level statements are executed at import
# time as opposed to when the program enters the
# view.
class UserViewSet(viewsets.ModelViewSet):
	print('storefront/quickstart/views.py UserViewSet')

	# API endpoint that allows users to be viewed or edited.
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	print('storefront/quickstart/views.py GroupViewSet\n')

	# API endpoint that allows groups to be viewed or edited.
	queryset = Group.objects.all().order_by('name')
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]