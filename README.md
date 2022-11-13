# HamraveshTask
Simulate command line tools for Docker with Django


Documentation:
https://documenter.getpostman.com/view/13169243/2s8YeuKAa5

Github Link:
https://github.com/pedy4000/HamraveshTask

Dockerhub Link:
https://hub.docker.com/repository/docker/pedyd/hamravesh-task/general



you can install and run with:

```
sudo docker pull pedyd/hamravesh-task:1.0
sudo docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock pedyd/hamravesh-task:1.0

```

or:

```
git clone https://github.com/pedy4000/HamraveshTask.git
sudo docker-compose -f compose.yaml up

```