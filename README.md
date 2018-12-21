# README

### Prerequisite Installation Instructions:

If not already done, install pip on your computer. 

#### Windows:
1) Check if you have pip installed. \
`py -m pip --version`

2)  Make sure pip is up-to-date. \
`py -m pip install --upgrade pip`

3) Install virtualenv \
`py -m pip install --user virtualenv`

4) Create a virtualenv. Direct to where pip python is installed by using 
command in step 1 \
`py -m virtualenv env`

5) To run python file from command line, activate virtualenv.
Direct to where pip python is installed by using command in step 1 \
`.\env\Scrips\activate` \
To confirm you're in the virtualenv, \
`where python`

6) Direct to project location, then execute file \
`python main.py`

#### Linux or MacOS
1) Check if you have pip installed. \
`python3 -m pip --version`

2) Make sure pip is up-to-date. \
`python3 -m pip --version`

3) Install virtualenv \
`python3 -m pip install --user virtualenv`

4) Create a virtualenv \
`python3 -m virtualenv env`

5) Activate virtualenv. Direct to project directory. \
`env/bin/activate` \
To confirm virtualenv location \
`which python`

6) Direct to project location, then execute file \
`python main.py`

#### To deactivate virtualenv in both Windows & Linux/MacOS:

`deactivate`


##### Referenced from https://packaging.python.org/guides/installing-using-pip-and-virtualenv/