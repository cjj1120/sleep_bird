Failed to Dockerize: 
# Build & Run Docker image 
docker build -t test-selenium .
docker run test-selenium 

# Remove docker image 
docker rmi -f test-selenium 

# Docker-compose appraoch: 
docker-compose up -d --no-deps --build
winpty docker exec -it fd07 bin/bash


https://medium.com/analytics-vidhya/deploy-a-selenium-based-crawler-to-docker-fd26f53f52e7
https://www.blazemeter.com/blog/selenium-docker