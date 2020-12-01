FROM python:3.9.0-alpine

WORKDIR /usr/src

ENV FLASK_APP=app/routes.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY Pipfile Pipfile.lock ./

RUN pip3 install pipenv && pipenv install --system --deploy

RUN pip3 install python-dotenv

EXPOSE 5000

COPY . .

CMD flask run