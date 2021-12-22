set PGPASSWORD=123456qQ
set errorlevel=

E:\PostgreSQL\13\bin\psql.exe -U postgres -c "drop database bfr;"
E:\PostgreSQL\13\bin\psql.exe -U postgres -c "create database bfr;"

E:\YandexDisk\biometric_face_recognition\venv\Scripts\python.exe E:\YandexDisk\biometric_face_recognition\manage.py makemigrations
E:\YandexDisk\biometric_face_recognition\venv\Scripts\python.exe E:\YandexDisk\biometric_face_recognition\manage.py migrate
E:\YandexDisk\biometric_face_recognition\venv\Scripts\python.exe E:\YandexDisk\biometric_face_recognition\scripts\init_data.py




