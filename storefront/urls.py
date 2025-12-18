from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from quickstart import views

# Routers provide an easy way of automatically
# determining the URL conf.
router = routers.DefaultRouter()

# Since the program uses viewsets instead of views, the
# URL conf for the API can be automatically generated
# through registering the viewsets with a router class.
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

# Customising the views for 404 and 500
# HTTP status codes will remove errors
# from being reported via email.

# Customise the view for an HTTP 404 error.
# handler404 = "polls.views.page_not_found"

# Customise the view for an HTTP 500 error.
# handler500 = "polls.views.internal_server_error"

# URLConf (URL Configuration)
urlpatterns = [
	path('admin/', admin.site.urls),

	# Any URLs that begin with 'playground/'
	# should be routed to the playground app.

	# When a request is made to the following URL, only
	# "hello" is sent to the urls.py module in the
	# "playground" app:
	# http://localhost:8000/playgroud/hello
	path('playground/', include('playground.urls')),

	# Wire up our API using automatic URL routing.
	# Additionally, we include login URLs for the browsable API.
	path('', include(router.urls)),

	# Configure the global URLconf in the storefront project
	# to include the URLconf defined in polls.urls.
	# include() chops off whatever part of the URL matched up
	# to that point and sends the remaining string to the
	# included URLconf for further processing.
	path("polls/", include("polls.urls"))
] + debug_toolbar_urls()