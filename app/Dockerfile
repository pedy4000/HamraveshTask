# # pull the official base image
# FROM python:3.8.3-alpine

# # create app directory
# RUN mkdir -p /home/app

# # copy project
# COPY . /home/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install dependencies
# RUN pip install --upgrade pip 
# RUN pip install -r /home/app/requirements.txt

# # install docker
# RUN apk update && apk add docker docker-compose openrc
# RUN rc-update add docker boot

# # expose port
# EXPOSE 80

# # run server
# CMD ["python", "/home/app/manage.py", "runserver", "0.0.0.0:80"]

# pull the official base image
FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder

# expose port
EXPOSE 8000

# ser work directory
WORKDIR /app 

# install dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

# copy project
COPY . /app 

# run server
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# update apk
FROM builder as dev-envs
RUN apk update && apk add git

# RUN  addgroup -S docker && adduser -S --shell /bin/bash --ingroup docker vscode

# install docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
CMD ["manage.py", "runserver", "0.0.0.0:8000"]