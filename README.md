# transaction dashboard

Python application to display fake transactions in basic HTML from a mock bank using the TrueLayer API.

## Installation

Download the project by git cloning:

```bash
$ git clone https://github.com/sarahseewhy/transaction-dashboard.git
```
The app dependency installation is managed by the Makefile.

Run `make install` from the root project directory to install the required Python dependencies.

## Usage

### Requirements

You must have `python3`, `pip3`, and `pipenv` installed in order to install, run, and test the application.

The application uses a `.env` file to set required environment variables.

Create a `.env` file in the root project directory and add the following configuration:

```text
CLIENT_ID=********
SECRET_ID=********
REDIRECT_URL=********
FLASK_ENV= development | production 
```

The `CLIENT_ID` and `SECRET_ID` values are found in the TrueLayer console. Please use the [TrueLayer documentation](https://docs.truelayer.com/#overview) to set this up.

`REDIRECT_URL` value will be a hostname (e.g., `localhost`) plus the redirect route configured in `routes.py` (in this case `authenticate/callback`). The value will need to also be set in the TrueLayer console.

You can decide whether to set the `FLASK_ENV` value to be "development" or "production" based on your needs.

### Installing dependencies

The project contains a Makefile which is used to install, run, and test the app.

First install the required packages from the root project directory:

```bash
$ make install
```

#### Running and testing

Run the app using the `run` Make command

```bash
$ make run
```

The Makefile is also responsible for running tests:

```bash
$ make test
```

## Roadmap

### Additional functionality

The app should display an aggregated set of all the transactions.

I did not get to this functionality yet, maybe next time!

### Testing

The app needs needs unit tests, integration tests (to the TrueLayer API), and Selenium-based tests to test the HTML rendering.

I began the TDD process but got stuck trying to stub and mock the TrueLayer API requests. I timeboxed the task but reached the limit of my Python testing knowledge and didn't want to exceed the timebox.  

### Logging

Even a basic layer of logging would help with debugging issues.

I used Python's `logging` library for debugging but decided against leaving it in the app.

There were some interesting debug situations where I could see a `400 Bad Request` response in the browser but it was not reflected in the logging. I'd love to get to the bottom of that.

### Error handling

The code is written optimistically and errors aren't handled with the try/catch blocks I'm used to seeing in Python.

The one block I added I ultimately removed because without tests I didn't have the same trust in its effectiveness.

### Caching and asynchronous API calls

I would've liked to implement async API calls to the TrueLayer API so it wouldn't be necessary to ask for the transaction data with every request.

Caching or saving data in a sensible manner would've also been a nice to have.

### Deployment

#### Docker

I initially added a Dockerfile and configured `docker-compose`. I successfully ran the app using Docker on Friday but when I returned on Sunday night to do some refactoring I got a `400 Bad Request` response from TrueLayer when I hit the `/authenticate` route.

I suspect the root cause is host configuration between the container, the app, and the allowed redirect URLs.

I've left the Dockerfile and the docker-compose.yml in the project for others to get a sense of the direction I took.

#### Terraform

The Python Flask app I worked on previously was deployed on AWS Lambda and I wanted to go in this direction.

It would've been fun to deploy the app to a Lambda but this was out of scope of the task. 