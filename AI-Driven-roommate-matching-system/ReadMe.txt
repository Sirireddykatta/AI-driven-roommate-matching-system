Download python latest version from python.org and install it.

Extract the zip into a folder in your desktop or any dir of choice.

Open the folder where the files were extracted using terminal.

Create the virtual environment by running the command

python -m venv venv

Activate the venv created

For windows

venv\Scripts\activate

For Ubuntu Linux

source venv/bin/activate

Install django in the activated environment

pip install django

Run the command

python manage.py runserver

You will see a link.

http://127.0.1.1.8000

Copy the link and open it in your browser