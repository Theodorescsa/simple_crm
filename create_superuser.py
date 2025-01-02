import os
import django
import environ

# Khởi tạo môi trường từ tệp .env
env = environ.Env()
environ.Env.read_env()
# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EzPDF.settings')
django.setup()

# Import model và sử dụng
from django.contrib.auth.models import User
username_admin = env('DJANGO_SUPERUSER_USERNAME')
username_email = env('DJANGO_SUPERUSER_EMAIL')
username_password = env('DJANGO_SUPERUSER_PASSWORD')
# Tạo superuser

try: 
    user_admin = User.objects.get(username = username_admin)
    print("Username is existed")
except Exception as e:
    User.objects.create_superuser(
        email=username_email,
        username=username_admin,
        password=username_password
    )
    print("Superuser created!")

