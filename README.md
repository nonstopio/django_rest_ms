# django_rest_ms
Creating MicroServices(MS) using Django REST framework.

### What are microservices? (http://microservices.io/)
Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture enables the continuous delivery/deployment of large, complex applications. It also enables an organization to evolve its technology stack.

  Since this is an example of MS, we have build three different Django projects team_ms, player_ms and match_ms where each project is an MS. As per MS architecture the data in every MS should be loosely coupled and have their own database. So, to make communication among MS we have made api calls.

## How to configure?
- Create virtual environment with pyhton3 in the root dir of the repo: `virtualenv env_worldcup -p python3`
- Dive into environment: `source env_worldcup/bin/activate`
- Install requirements: `pip install requirements.txt`
- Do database migrations, since, we have 3 projects go in every project and migrate the data as follows:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

## How to run?
- Since, it is MS, run the projects seperately on different ports. Again go in every project and run the command `python manage.py runserver 127.0.0.1:<your port number>`
- Every MS has a file `common.py`, for example Player MS has it in `player_ms/player_app/services/common.py`. Change the URLs accordingly

## Populate data!
It is important to populate the data before understanding the scenarios. Goto respective urls and populate the data using Django REST Framework Interface.

In addition to your records, if you with to check with too many players, call the api `<player ms url>/fake_200_players/`.

## Scenarios
This application has mainly three modules Team, Player and Match which are converted to MS. All modules are related to each other like, a team has list of players, every player has a team assigned to him/her, every match has two teams.

- *Get team details*
  - API: `<team ms url>/get_team_details/<team_id>`
  - This api fetches the details about the team and list of players in that team. But, players' data reside in Player MS. So api for list of players is called `<player ms url>/get_team_players/<team id>/`
  
- *Get all players*
  - API: `<player ms url>/get_players/`
  - This api fetched the list of all the players in the WorldCup. But, every player is assigned a team and the team's data resides in Team MS. So, we call the Team MS api from Player MS: `<team ms url>/get_player_team/`

- *Get all match*
  - API: `<match ms url>/get_all_match/`
  - This api fetches list of all the matches in the WorldCup. But, every match has two teams which again reside in Team Ms. So we call have called Team MS api from Match MS: `<team ms url>/get_match_team/`
