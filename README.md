## Running Locally
Make sure you have Python 3.8.7 installed locally. 

```sh
$ git clone https://github.com/Reof07/oferton_vip.git
$ cd oferton_vip

$ python3 -m venv  myvenv # NOTA: if you're using windons is python -m ....
$ pip install -r requirements.txt

# You must crearte a file .env  in BASE_DIR and put inside: 
SECRET_KEY_DJANGO=your secret key
SAMPLE_SECRET_KEY=your secret key

$ pyhton mange.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```
