FROM python:3.10.3-slim-buster as base
# Set enviroment
RUN apt-get update 
RUN pip install --upgrade pip

RUN  pip install poetry
COPY . /app/
WORKDIR /app



RUN poetry install





FROM base as development 
EXPOSE 4000

CMD ["poetry", "run", "flask","run","--host=0.0.0.0"]

FROM base as production
CMD ["poetry", "run","gunicorn", "todo_app.app:app", "-b", "0.0.0.0:5000"]

FROM base as test


CMD ["poetry", "run", "pytest"]







