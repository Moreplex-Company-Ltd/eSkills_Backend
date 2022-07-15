# #!/bin/bash

# source '/var/app/venv/staging-LQM1lest/bin/activate' && {
#     if [[ $EB_IS_COMMAND_LEADER == "true" ]];
#     then
#         # log which migrations have already been applied
#         python3 /var/app/current/manage.py showmigrations;
#         # migrate
#         python3 /var/app/current/manage.py migrate --noinput;
#     else 
#     echo "this instance is NOT the leader";
    
#     fi
# }