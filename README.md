# grexter
## Portal to add Buildings & Rooms.

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

To access the API : 
## Buildings

1) GET all buildings: https://grexter-shashank.herokuapp.com/api/v1/buildings/

2) GET one building by id : https://grexter-shashank.herokuapp.com/api/v1/buildings/1/

3) Create building:
POST : https://grexter-shashank.herokuapp.com/api/v1/buildings/

```
{"name": "Aquila", "address": "HSR layout, Bangalore", "landmark_1": "6th sector"}
```
4) Update Building:
PUT : https://grexter-shashank.herokuapp.com/api/v1/buildings/<building_id>
```
{"name": "Aquila", "address": "BTM Layout, Bangalore", "landmark_1": "5th sector"}
```
5) Delete Building : 
DELETE : https://grexter-shashank.herokuapp.com/api/v1/buildings/<building_id>

## Rooms

1) GET all rooms : https://grexter-shashank.herokuapp.com/api/v1/rooms/

2) GET one room by id : https://grexter-shashank.herokuapp.com/api/v1/rooms/1/

3) Create Room :
POST : https://grexter-shashank.herokuapp.com/api/v1/rooms/

```
{"building_id": 2,
"flat_number": "101",
"sqft_area": 600,
"rent": 10000,
"flat_type": "1BHK",
"bathrooms": 2,
"ec_acc_number": "QWERpoiu"}
```
4)Update Room 
PUT : https://grexter-shashank.herokuapp.com/api/v1/rooms/1/

```
{"flat_number": "101",
"sqft_area": 700,
"rent": 15000,
"flat_type": "2BHK",
"bathrooms": 2,
"ec_acc_number": "QWERpoiu"}
```
5) Delete Room 
DELETE : https://grexter-shashank.herokuapp.com/api/v1/rooms/1/


