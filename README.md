## Prerequisite
1. Installed Python and pip.
  - Python download page - [link](https://www.python.org/downloads/)
  - Check version after install python
    ```sh
    $python --version
    Python 2.7.6
    ```
  
  - pip install document - [link](https://pip.pypa.io/en/latest/installing.html#using-the-installer)
  
    > download "get-pip.py"
    ```sh
    $wegt https://bootstrap.pypa.io/get-pip.py
    ```
    > install pip
    ```sh
    $python get-pip.py
    ```
  
2. Installed Django framework.
  - install page - [link](https://django-doc-pootle-test.readthedocs.org/en/latest/topics/install.html#installing-official-release)
  
    ```sh
    $sudo pip install Django
    ```
  
## Run
1. Running the Develoment Server

  in youre project directory
  ```sh
  $python manage.py runserver
  ```
  
  If installed, You’ll see something like this:
  ```
  June 18, 2015 - 22:31:22
  Django version 1.8.2, using settings 'crm.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```
  
2. View page

  open browser in your computer (recomend ***Crome browser*** )
  
  type string below in address bar
  ```
  http://localhost:8000
  ```
  
