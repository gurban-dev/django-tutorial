Strategy for Solving Django Assessments

1. First determine what behavior in the project needs to change.

2. Understand exactly what the TODO functions are responsible for.

3. Inspect the surrounding class behavior.

Example:

Users should only be able to modify snippets that they own.
The snippet list endpoint should support filtering by programming
language.

Add comments explaining any non-obvious implementation decisions.

A snippet is just a small piece of code.

The serializer is a layer that translates between Python/Django
objects and the data that comes into or out of an API.

Python/Django object
-> Serializer
-> JSON data

SnippetList in views.py is an API view. Its responsibility is to
handle an HTTP request and decide what should happen.
For a GET request, snippets may be retrieved, while a POST may
create a snippet.

Conceptually:
HTTP request

->

SnippetList

->

Serializer / Model

->

HTTP response

An API view receives an HTTP request and decides what response
to send back. It's specifically for sending and receiving data
like JSON instead of rendering an HTML page.