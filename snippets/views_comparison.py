from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# This function-based view handles both GET and POST requests.
@api_view(["GET", "POST"])
def snippet_list(request):

    # The GET behavior is implemented directly inside the function.
    if request.method == "GET":
        snippets = Snippet.objects.all()

        # Convert the Snippet objects into JSON-compatible data.
        serializer = SnippetSerializer(snippets, many=True)

        return Response(serializer.data)

    # The POST behavior is also implemented directly inside the
    # function.
    serializer = SnippetSerializer(data=request.data)

    # Validation and object creation are handled explicitly here.
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# This class-based view inherits reusable behavior from DRF.
class SnippetList(generics.ListCreateAPIView):

    # Configure which objects the view operates on.
    queryset = Snippet.objects.all()

    # Configure which serializer the view uses.
    serializer_class = SnippetSerializer

    # ListCreateAPIView already provides reusable behavior for
    # listing and creating objects.

    # We do not need to implement the GET and POST logic ourselves.
    # We only configure the behavior that is specific to our model.


# Function-based view:

# The GET and POST behavior is implemented directly inside
# the function.

# Reusing this behavior in another view would require us to
# write or extract that logic ourselves.


# Class-based view:

# ListCreateAPIView already provides reusable behavior for
# listing and creating objects.

# The class inherits that behavior and only needs to configure
# the queryset and serializer.


# FUNCTION-BASED VIEW

# snippet_list()
#     |
#     +-- GET logic
#     |
#     +-- POST logic
#     |
#     +-- validation
#     |
#     +-- serialization
#     |
#     +-- response handling


# CLASS-BASED VIEW

# SnippetList
#     |
#     +-- inherits ListCreateAPIView
#             |
#             +-- list behavior
#             |
#             +-- create behavior
#             |
#             +-- validation and response handling

# Why is the class-based view more reusable?

# DRF defines the common GET and POST behavior once inside
# ListCreateAPIView. Many different views can inherit that same
# behavior without implementing it again.

# For example, another model can reuse the exact same behavior
# by creating another ListCreateAPIView and changing only its
# queryset and serializer.