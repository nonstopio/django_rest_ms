virtualenv env_worldcup -p python3
source env_worldcup/bin/activate
pip install requirements.txt
python ./team_ms/manage.py runserver 127.0.0.1:7001 &
python ./player_ms/manage.py runserver 127.0.0.1:7002 &
python ./match_ms/manage.py runserver 127.0.0.1:7003 &
deactivate

