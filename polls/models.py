from django.db import models

import datetime

from django.utils import timezone

# Create your models here.

class Question(models.Model):

  # question_text is a field.
  # Assuming there "QuestionAdmin" is not registered
  # "question_text" should appear vertically before
  # "pub_date" because it is declared first.
  question_text = models.CharField(max_length=200)

  # pub_date (publication date) is the second field.
  pub_date = models.DateTimeField("date published")

  def was_published_recently(self):
    print("pub_date:", self.pub_date)
    # print("timezone.now() - datetime.timedelta(days=1):", timezone.now() - datetime.timedelta(days=1))
    # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    now = timezone.now()

    # Returns true if self.pub_date is less than the current time,
    # but also greater than the exactly twenty-four hours ago.
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Evaluates to "False".
    # return 2 >= 3

  # Adding __str__() methods to your models makes it
  # reveals more data when dealing with the Python
  # interactive shell.

  # The following method is invoked when the following line
  # is executed:
  # Question.objects.all()
  def __str__(self):
    # The following is outputted in the interactive Python
    # shell:
    # <QuerySet [<Question: What's up?>]>

    # If it weren't for this method, the following would be
    # outputted instead:
    # <QuerySet [<Question: Question object (1)>]>
    return self.question_text


class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  choice_text = models.CharField(max_length=200)

  # "votes" is a field in a database table.
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text