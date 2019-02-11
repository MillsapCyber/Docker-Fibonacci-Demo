# Docker-Fibonacci-Demo
A quick demo of how cool docker is using a simple load-balanced php app and a python api 

# Load-Balancer
- By using docker-compose scale and an Nginx proxy (included in the repo), we can achieve round robin DNS load balancing. Just launch the app with the following command
- ``docker-compose up --scale app=4 --scale api=4``
