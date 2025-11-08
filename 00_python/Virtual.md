Virtual Env?

It's like safeguarding your
application from other versions
and don't clutter your operating
system and also so that your
program actually moves safely in
other environment as well on
Linux, on Mac or other people's
computer.

Step 1: Open Terminal / Command Prompt

Make sure Python 3 is installed.
Check by running:

python --version


or sometimes:

python3 --version

Step 2: Go to your project folder
cd path/to/your/project


Example:

cd Desktop/myproject

Step 3: Create Virtual Environment

Windows:

python -m venv venv


Mac / Linux:

python3 -m venv venv


This will create a folder named venv/ inside your project.

Step 4: Activate the Virtual Environment

Windows (CMD / PowerShell):

venv\Scripts\activate


Mac / Linux:

source venv/bin/activate


After activation, your terminal will show something like:

(venv) C:\Users\You\Desktop\myproject>


This means the virtual environment is active.

Step 5: Install Packages Inside Virtual Env

Example:

pip install flask

Step 6: Save Dependencies

Create a requirements.txt:

pip freeze > requirements.txt

Step 7: Deactivate Virtual Env (When you're done)
deactivate

Later: Recreate Virtual Env from Requirements
pip install -r requirements.txt