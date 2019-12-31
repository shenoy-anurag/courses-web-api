# Courses
My first Django Web App. The app allows users to access an api to create courses and lectures.

In order to run this Django App, you will need to do the following:

1. Clone or download the repository.
2. Open the folder as a project in a Python IDE.
3. Create a Virtual Environment and install the required packages.
   1. Open a terminal in the project directory.
   2. Run `python3 -m venv venv`. This will create a virtual environment named 'venv'.
   3. Run `source venv/bin/activate`. This will activate the virtual environment. Your should be able to see `(venv)` at the beginning.
   4. Execute `pip3 install -r {{path_to_requirements_file}}/requirements.txt`. Don't forget to replace `{{path_to_requirements_file}}` with the path to the requirements file.
4. Set your IDE to use the newly created Virtual Environment. In PyCharm, click on File > Settings > Project > Project Interpreter and Select the virtual environment you just created.
5. Execute `python3 manage.py runserver`.
6. Open the link provided in the terminal or go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You can now Explore the APIs from the API Root and play around by performing CRUD operations.
