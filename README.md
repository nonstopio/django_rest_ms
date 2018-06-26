# django_rest_ms
Creating MicroServices(MS) using Django REST framework.

### What are microservices? (http://microservices.io/)
Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture enables the continuous delivery/deployment of large, complex applications. It also enables an organization to evolve its technology stack.

  Since this is an example of MS, we have build three different Django projects team_ms, player_ms and match_ms where each project is an MS. As per MS architecture the data in every MS should be loosely coupled and have their own database. So, to make communication among MS we have made api calls.

## How to configure?
- Create virtual environment with pyhton3 in the root dir of the repo: `virtualenv env_worldcup -p python3`
- Install requirements: `pip install requirements.txt`
- Do database migrations, since, we have 3 projects go in every project and migrate the data as follows:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

## How to run?
Since, it is MS, run the projects seperately on different ports. Again go in every project and run the command `python manage.py runserver 127.0.0.1:<your port number>`
