from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# Purpose: To serialize and deserialize the snippet
# instances into representations such as json.
class SnippetSerializer(serializers.Serializer):
  # Define the fields that get serialized/deserialized.
  id = serializers.IntegerField(read_only=True)

  # Note that required, max_length, and
  # default are called validation flags.
  title = serializers.CharField(
    required=False,
    allow_blank=True,
    max_length=100)

  # Controls how the browsable API should be displayed.
  code = serializers.CharField(style={'base_template': 'textarea.html'})

  linenos = serializers.BooleanField(required=False)

  language = serializers.ChoiceField(
    choices=LANGUAGE_CHOICES, default='python')

  style = serializers.ChoiceField(
    choices=STYLE_CHOICES, default='friendly')

  # Note that either create() or update() is
  # invoked when serializer.save() is called.

  def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given
    the validated data."""

    # -Why do two asterisks precede "validated_data"?
    return Snippet.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
    Update and return an existing `Snippet` instance,
    given the validated data."""
    instance.title = validated_data.get('title', instance.title)
    instance.code = validated_data.get('code', instance.code)
    instance.linenos = validated_data.get('linenos', instance.linenos)
    instance.language = validated_data.get('language', instance.language)
    instance.style = validated_data.get('style', instance.style)
    instance.save()
    return instance

# ModelSerializer classes are simply a shortcut
# for creating serializer classes:
# An automatically determined set of fields.
# Simple default implementations for the create() and update() methods.
# class SnippetSerializer(serializers.ModelSerializer):
#   # An "owner" field exists because snippets
#   # are associated with a user.
#   owner = serializers.ReadOnlyField(source='owner.username')

#   class Meta:
#     model = Snippet
#     fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#       model = User
#       # Because 'snippets' is a reverse relationship on the
#       # User model, it will not be included by default when
#       # using the ModelSerializer class, so we needed to add
#       # an explicit field for it.
#       fields = ['id', 'username', 'snippets']