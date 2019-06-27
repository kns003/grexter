# grexter
Portal to add Buildings & Rooms.

1. Clone the repository and intall virtualenv with Python3.5 and activate it
  - `virtualenv -p /usr/bin/python3.5 venv_grexter
  - `source venv_grexter/bin/activate
2. Install the requirements. `pip install -r requirements.txt`
3. Run the migrations. `python manage.py migrate`
4. Create a superuser to login. `python manage.py createsuperuser`. Follow the instructions and remember the username and password to login

5. Run the management server. `python manage.py runserver`
6. Navigate in the browser - `127.0.0.1:8000`
7. Enter the username and password & you can add building and rooms.
8. In Building & Room Listing page, search & filters are provided.

This project is also hosted on Heroku : https://grexter-shashank.herokuapp.com/
