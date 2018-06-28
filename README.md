# django_rest_ms
Creating MicroServices(MS) using Django REST framework.

### What are microservices? (http://microservices.io/)
Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of loosely coupled services, which implement business capabilities. The microservice architecture enables the continuous delivery/deployment of large, complex applications. It also enables an organization to evolve its technology stack.

  Since this is an example of MS, we have build three different Django projects team_ms, player_ms and match_ms where each project is an MS. As per MS architecture the data in every MS should be loosely coupled and have their own database. So, to make communication among MS we have made api calls.

## How to configure?
  - Run below command:
    - `git clone https://github.com/nonstopio/django_rest_ms.git`
    - `cd django_rest_ms`
    - `./zero_config.bash`
  - There you go. Everything is set. Refer following URLs for respective MS:
    - Team MS: http://127.0.0.1:7001/
    - Player MS: http://127.0.0.1:7002/
    - Match MS: http://127.0.0.1:7003/

**NOTE: These servers will run in background so to stop the servers run: `pkill -f manage.py`**

## Scenarios
This application has mainly three modules Team, Player and Match where every module is an MS. All modules are related to each other like, a team has list of players, every player has a team assigned to him/her, every match has two teams.

- *Get team details*
  - API: http://127.0.0.1:7001/get_team_details/2/
  - This api fetches the details about the team and list of players in that team. But, players' data reside in Player MS. So api for list of players is called `http://127.0.0.1:7002/get_team_players/1/`
  
- *Get all players*
  - API: http://127.0.0.1:7002/get_players/
  - This api fetched the list of all the players in the WorldCup. But, every player is assigned a team and the team's data resides in Team MS. So, we call the Team MS api from Player MS: `http://127.0.0.1:7001/get_player_team/`

- *Get all match*
  - API: http://127.0.0.1:7003/get_all_match/
  - This api fetches list of all the matches in the WorldCup. But, every match has two teams which again reside in Team Ms. So we call have called Team MS api from Match MS: `http://127.0.0.1:7001/get_match_team/`


# Docker

- Create services: `docker-compose run player_web . ` (Player_web depends on team_web and match_web. So, all services will be created)
- Run services: `docker-compose up` (To run in background append with `-d`)
- Stop services (Gracefully): `docker-compose down`
