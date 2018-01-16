This package is an optional dependency for the muonic package. 
It provides an example project to be used with the muonic_django package. 

To start rabbit mq (needed for tasks): sudo docker run --hostname localhost -p 0.0.0.0:5672:5672 rabbitmq

To run celery worker (for tasks): celery -A muonic_web worker -l info. Make sure the PYTHONOPTIMIZE environment variable is set to 1 (export PYTHONOPTIMIZE=1)

To set up the project: muonic_webapp migrate; muonic_webapp createsuperuser

To run Django: muonic_webapp runserver (then visit http://localhost:8000)
