#! /usr/bin/python3
'''
--virtual enviroments--
--create then activate enviroment
python3 -m venv venv_file
source venv_file/bin/activate
-- run app
export FLASK_APP=main.py
export FLASK_ENV=development
flask run

'''

from webif import rover_app

app = rover_app()#ref from init.py

if __name__ == '__main__':# run this file directly
    try:
        app.run(debug = True,host = "192.168.0.197", port = 5000) # auto rerun of webapp when changes occur
    except OSError:
        app.run(host = "192.168.0.197", port = 5001)
    except KeyboardInterrupt:
        print('User Stop')
        
