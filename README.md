# keycode_2023
repository for BE keycode-2023

<br />

##Setting up a dev environment:
- Install python (preferably 3.10 or higher)
- Clone the project
- Create a python virtual environment - python3 -m venv venv
- Activate the virtual environment - source venv/bin/activate
- Install required dependencies: pip install -r requirements.txt
- Modify the .env file as needed. Follow steps below.
- Set FLASK_DEBUG=True in .flaskenv to turn on hot reload


##Setting .env file
- Set DATABASE_URL = 'postgresql+psycopg2://{username}:{password}@localhost/{database_name}'. Remove the '{}' from the URL.
- Set ENV = 'development'


##Commands:
- Run the application - flask run
- Run a flask shell - flask shell
- Initialise migrations folder - flask db init
- Create migratrion - flask db migrate
- Apply migration - flask db upgrade
