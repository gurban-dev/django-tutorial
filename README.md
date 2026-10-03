Create a virtual environment:

python -m venv <name_of_virtual_environment>

E.g.
python -m venv .django-venv

Install all of the dependencies:

pip install -r requirements.txt


Launch the local development server:

python manage.py runserver


Run the following if the SECRET_KEY is not
being read from the environment variables
file:

source ~/.bash_profile