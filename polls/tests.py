import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() returns False for
    questions whose pub_date is in the future.
    """
    time = timezone.now() + datetime.timedelta(days=30)

    print(f"\nfuture_question time: {time}\n")

    # Create a Question instance with a
    # pub_date that is thirty days from now.
    future_question = Question(pub_date=time)

    # Check the output of was_published_recently() which
    # ought to be False as the second argument asserts.

    # The subsequent test case will fail if the
    # was_published_recently() method returns
    # something other than False.
    self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for
    questions whose pub_date is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)

    print(f"\nold_question time: {time}\n")

    # Create a Question object with a pub_date
    # that was one day and one second ago.
    old_question = Question(pub_date=time)

    self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions
    whose pub_date is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)

    print(f"\nrecent_question time: {time}\n")

    # Instantiate an instance of the Question class with a pub_date
    # that was 23 hours, 59 minutes, and 59 seconds ago.
    recent_question = Question(pub_date=time)

    self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
  """
  Create a Question object with the given `question_text` and
  published the given number of `days` offset to now (negative
  for questions published in the past, positive for questions
  that have yet to be published).
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
  def test_no_questions(self):
    """
    If no questions exist, an appropriate message is displayed.
    """

    # Use Django's test Client to make an HTTP GET request:
    # http://127.0.0.1:8000/polls/
    response = self.client.get(reverse("polls:index"))

    # Check if the request was successfully processed.
    self.assertEqual(response.status_code, 200)

    print(f'\ntest_no_questions response: {response}\n')

    print(f'\ntest_no_questions response.context: {response.context}\n')

    # Verify if the HTTP response contains certain content.
    self.assertContains(response, "No polls are available.")

    # Make sure the "latest_question_list" key in
    # the response dictionary has an empty value.
    self.assertQuerySetEqual(response.context["latest_question_list"], [])

  def test_past_question(self):
    """
    Questions with a pub_date in the past are displayed on the
    index page.
    """
    # Question instance published thirty days ago.
    question = create_question(question_text="Past question.", days=-30)

    # Make an HTTP request:
    # http://127.0.0.1:8000/polls/
    response = self.client.get(reverse("polls:index"))

    # response.context["latest_question_list"] contains:
    # <QuerySet [<Question: Past question.>]>

    # assertQuerySetEqual(qs, iterOfValues) asserts that a queryset
    # qs matches a particular iterable of values iterOfValues.
    self.assertQuerySetEqual(
      response.context["latest_question_list"],
      [question],
    )

  def test_future_question(self):
    """
    Questions with a pub_date in the future aren't displayed on
    the index page.
    """
    create_question(question_text="Future question.", days=30)

    response = self.client.get(reverse("polls:index"))

    self.assertContains(response, "No polls are available.")
    self.assertQuerySetEqual(response.context["latest_question_list"], [])

  def test_future_question_and_past_question(self):
    """
    Even if both past and future questions exist, only past questions
    are displayed.
    """
    question = create_question(question_text="Past question.", days=-30)

    # The question with a publication date
    # in the future won't be displayed.
    create_question(question_text="Future question.", days=30)

    response = self.client.get(reverse("polls:index"))

    # response.context["latest_question_list"] contains:
    # <QuerySet [<Question: Past question.>]>

    self.assertQuerySetEqual(
      response.context["latest_question_list"],
      [question],
    )

  def test_two_past_questions(self):
    """
    The questions index page may display multiple questions.
    """
    question1 = create_question(question_text="Past question 1.", days=-30)
    question2 = create_question(question_text="Past question 2.", days=-5)

    # http://127.0.0.1:8000/polls/
    response = self.client.get(reverse("polls:index"))

    self.assertQuerySetEqual(
      response.context["latest_question_list"],
      [question2, question1],
    )


class QuestionDetailViewTests(TestCase):
  def test_future_question(self):
    """
    The detail view of a question with a pub_date in the future
    returns a 404 not found.
    """
    future_question = create_question(question_text="Future question.", days=5)

    # url = http://127.0.0.1:8000/polls/2/
    url = reverse("polls:detail", args=(future_question.id,))

    response = self.client.get(url)

    # If response.status_code is not equal
    # to 404, this test case fails.
    # A 404 HTTP response indicates that the
    # request was not successfully processed.
    self.assertEqual(response.status_code, 404)

  def test_past_question(self):
    """
    The detail view of a question with a pub_date in the past
    displays the question's text.
    """
    past_question = create_question(question_text="Past Question.", days=-5)

    # url = http://127.0.0.1:8000/polls/2/
    url = reverse("polls:detail", args=(past_question.id,))

    # "response" is a Python representation of an HTTP response.
    # Return value of "response":
    # <TemplateResponse status_code=200, "text/html; charset=utf-8">
    response = self.client.get(url)

    print(f"\nQuestionDetailViewTests response: {response}\n")

    print(f"\nQuestionDetailViewTests response.content: {response.content}\n")

    # If the response contains the value returned from
    # past_question.question_text, it shows that the GET
    # request was successful because a response consisting
    # of "Past Question" was sent back from the web server.
    self.assertContains(response, past_question.question_text)