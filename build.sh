set -o errexit

pip install -r requirements.txt


python manage.py collectstation --no-input
python manage.py migrate