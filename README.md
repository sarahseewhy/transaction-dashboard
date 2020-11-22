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

**Requirements**: `python3`, `pipenv`

The app can be built and run using the Makefile.

First install the required packages from the root project directory:

```bash
$ make install
```

Run the app using the `run` Make command

```bash
$ make run
```

## Roadmap

### Testing

The app needs needs unit tests, integration tests (to the TrueLayer API), and Selenium-based tests to test the HTML rendering.

I began the TDD process but got stuck trying to stub and mock the TrueLayer API requests. I timeboxed the task but reached the limit of my Python testing knowledge and didn't want to exceed the timebox.  

### Logging

Even a basic layer of logging would help with debugging issues.

I used Python's `logging` library for debugging but didn't get to implement it.

There were some interesting debug situations where I could see a `400 Bad Request` response in the browser but it was not reflected in the logging. I'd love to get to the bottom of that.

### Error handling

The code is written optimistically and errors aren't handled with the try/catch blocks I'm more used to seeing in Python.

The one I did add I ultimately removed because without tests I didn't have the same trust in its effectiveness.

### Caching and asynchronous API calls

I would've liked to implement async API calls to the TrueLayer API so it wouldn't be necessary to ask for the transaction data with every request.

### Deployment

#### Docker

I initially added a Dockerfile and configured docker-compose. I successfully ran the app using Docker on Friday but when I returned on Sunday night to do some refactoring I got a `400 Bad Request` response from TrueLayer when I hit the `/authenticate` route.

I suspect the root cause is host configuration between the container, the app, and the allowed redirect URLs.

I've left the Dockerfile and the docker-compose.yml in the project to get a sense of the direction I took.

#### Terraform

The Python Flask app I worked on previously was deployed on AWS Lambda and I wanted to go in this direction. 

## License
[MIT](https://choosealicense.com/licenses/mit/)