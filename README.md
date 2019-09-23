# Bungalow

## Setup local environment

1. Install python3.6.8

2. Install postgresql10.10

3. Create admin user for the database, run the following sql statements.
```sql
CREATE DATABASE bgdb;
CREATE USER admin WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE bgdb TO admin;
```
4. Create and activate a virtual envionment.
```bash
python3.6 -m venv env
source env/bin/activate
```
5. Install all dependences
```bash
pip3.6 install -r requirements_dev.txt
```
6. Make a configure file in the path /etc/bg_settings/settings.ini

7. Copy all contents from settings.ini.sample to the settings.ini file.

8. Make migrations and migrate all data
```bash
python3.6 manage.py showmigrations
python3.6 manage.py migrate
python3.6 manage.py makemigrations
python3.6 manage.py migrate
```
9. Create a new superuser by using django command
```bash
python3.6 manage.py createsuperuser
```
10. Import the bungalow data
```bash
python3.6 manage.py import_bg_data
```
11. Run pytest to make sure all test cases work properly
```bash
pytest
```
12. Run django collectstatic
```bash
python3.6 manage.py collectstatic
```
13. Run django server
```bash
python3.6 manage.py runserver 0:8080
```
14. Visit http://localhost:8080/api/login/
log in by using your created user.

15. You are good to go to test the apis.  You can also visit the http://ec2-18-216-84-21.us-east-2.compute.amazonaws.com/api/login/
```
username: admin
password: Welcome0!
```
## The major features
You can create, query, filter, and sort the bungalow records. 
