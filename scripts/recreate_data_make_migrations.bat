set PGPASSWORD=123456qQ
set errorlevel=

c:\"Program Files"\PostgreSQL\14\bin\psql.exe -U postgres -c "drop database bfr;"
c:\"Program Files"\PostgreSQL\14\bin\psql.exe -U postgres -c "create database bfr;"

..\venv\Scripts\python.exe C:\BFR\biometric_face_recognition\manage.py makemigrations
..\venv\Scripts\python.exe C:\BFR\biometric_face_recognition\manage.py migrate
..\venv\Scripts\python.exe C:\BFR\biometric_face_recognition\scripts\init_data.py



