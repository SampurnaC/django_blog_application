# Django Blog Application




https://github.com/SampurnaC/django_blog_application/assets/11813341/c92a966b-e764-424e-828b-d61afbb129d9



## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:SampurnaC/django_blog_application.git
$ cd django_blog_application
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/bin/activate
```

Then run docker to start the web server, install dependencies and start other services like elasticsearch, redis, and celery.

```sh
sudo docker-compose up --build
```

And navigate to `http://localhost:8000`.
```



