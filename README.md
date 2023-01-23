# Django-REST-API

A Django REST API for power meters. It allows you to register new meters as well as measurements, and get data such as average or peak consumption, and delete any of them as well.

# Running the project

To get up and running straigth away:
1. Clone the repo.
2. Navigate to the root folder.
3. Confirm that you have installed virtualenv globally. If not, run this:
```bash
        $ pip install virtualenv
 ```
5. Create and fire up your virtual environment:
 ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
 ```
6. Install the dependencies needed to run the app:
```bash
            $ pip install -r requirements.txt
```         
7. Make those migrations work
```bash
            $ py manage.py makemigrations
            $ py manage.py migrate
```
8. Run:
```bash
            $ py manage.py runserver
```
9. You may use the API manually, or by using a client such as Thunder Client

