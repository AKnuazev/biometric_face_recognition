set PGPASSWORD=123456qQ
set errorlevel=

c:\"Program Files"\PostgreSQL\14\bin\psql.exe -U postgres -c "drop database bfr;"
c:\"Program Files"\PostgreSQL\14\bin\psql.exe -U postgres -c "create database bfr;"

..\venv\Scripts\python.exe ..\..\manage.py migrate
..\venv\Scripts\python.exe ..\scripts\init_data.py



