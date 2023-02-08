#! bin/sh
gunicorn --chdir /flask -b:5000 app:app