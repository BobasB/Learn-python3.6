FROM python:3.7-stretch
RUN pip install pipenv

WORKDIR /app

COPY . .

RUN pipenv install --system --deploy --clear

ENTRYPOINT ["python", "graph_experiments"]