Synonym App

A simple Flask application that allows users to find synonyms for a given word. This app uses Datamuse API to find the synonyms.

Following are the prerequisites while creating Synonym App.

- Python 3
- Git

To run Synonym App from local machine

1.  Open Terminal.
2.  Change the current working directory to the location where you want the cloned directory.
3.  Type `git clone https://github.com/sanjaykarki/synonym_app.git` and press **Enter** to create your local clone

    ```
    $ git clone https://github.com/sanjaykarki/synonym_app.git
    Cloning into 'synonym_app'...
    remote: Enumerating objects: 17, done.
    remote: Counting objects: 100% (17/17), done.
    remote: Compressing objects: 100% (13/13), done.
    remote: Total 17 (delta 6), reused 12 (delta 3), pack-reused 0
    Receiving objects: 100% (17/17), 23.77 KiB | 4.75 MiB/s, done.
    Resolving deltas: 100% (6/6), done.
    ```

4.  Type `cd synonym_app` to change working directory to synonym_app and set up a virtual environment to isolate the project’s dependencies.
    - For macOS/Linux
      ```
      $ python3 -m venv venv
      $ . venv/bin/activate
      ```
    - For Windows
      ```
      > py -3 -m venv venv
      > venv\Scripts\activate
      ```
5.  Install required dependency using `pip install -r requirements.txt`
6.  Run the application using `flask run`
    ```
    $ flask run
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```
7.  Visit `http://127.0.0.1:5000` in your browser to see the application.

  <img width="1414" alt="synonym-app" src="https://user-images.githubusercontent.com/4466090/215365262-943e13f0-d1c4-466e-8914-fa2c7952259e.png">
