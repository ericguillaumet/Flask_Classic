# Incomes-Expenses web APP

Software built in Python with the framework Flask, Hello World

## Install

- In the Python environment, execute command:

```
pip install -r requirements.txt
```

The used libraries: https://flask.palletsprojects.com/en/2.2.x/


## Rename the file .env_template to .env and add the following lines:
```
FLASK_APP=main.py
FLASK_DEBUG=True
```

## Command to execute the server:

```
flask --app main run
```

# Command to execute the server live:

```
flask --app main --debug run 
```

## Command to run the server in a different port:

```
flask --app main run -p 5001
```

## Command to run the debug mode in the changed port:

```
flask --app main --debug run -p 5001
```