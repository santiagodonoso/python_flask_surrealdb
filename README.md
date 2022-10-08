# python_flask_surrealdb
Create a virtual environment
> python -m venv .

Start the virtual environment in Windows
> Scripts\activate

Install the required python libraries
> python install -r requirements

Download SurrealDB
Check their website for instructions

Start the SurrealDB server
> surreal start --log trace --user admin --pass password file:data

Run the app
> python app.py

To connect to SurrealDB from the terminal
> surreal sql --conn http://localhost:8000 --user admin --pass password --ns company --db company --pretty


