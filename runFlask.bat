set root=C:\Users\Dell\Anaconda3

call %root%\Scripts\activate.bat %root%

set FLASK_ENV=development
set FLASK_DEBUG=1

cd Engine
python main.py

pause