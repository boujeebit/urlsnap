
#!/bin/bash

# ------------------------------------------
# Author: Mickey Hefley
# Description: Simple script to clean all
# images and containers off a local machine
# ------------------------------------------

docker rm $(docker ps -a -q)
docker rmi $(docker images -q)