from django.forms.models import model_to_dict
from django.db import utils
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework import status
from .models import App
import docker
import json

client = docker.from_env()

class AppViewSet(ViewSet):
    def create(self, request: Request):
        try:
            app = App.objects.create(**request.data)
            app.save()
            return Response(model_to_dict(app), status=status.HTTP_201_CREATED)
        except utils.IntegrityError as err:
            return Response("duplicate name for app", status=status.HTTP_409_CONFLICT)

    def list(self, request):
        appsList = [model_to_dict(app) for app in App.objects.all()]
        return Response(appsList, status=status.HTTP_200_OK)

    def get(self, request, id: str):
        try:
            return Response(model_to_dict(App.objects.get(id=id)), status=status.HTTP_200_OK)
        except App.DoesNotExist as err:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

    def delete(self, request, id: str='-1'):
        try:
            app = App.objects.get(id=id)
            res = model_to_dict(app)
            app.delete()
            return Response(res, status=status.HTTP_200_OK)
        except App.DoesNotExist as err:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def edit(self, request, id: str='-1'):
        try:
            app = App.objects.get(id=id)
            for key in model_to_dict(app):
                if key in request.data:
                    setattr(app, key, request.data[key])
                    
            app.save()
            return Response(model_to_dict(app), status=status.HTTP_200_OK)
        except App.DoesNotExist as err:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except utils.IntegrityError as err:
            return Response("duplicate name for app", status=status.HTTP_409_CONFLICT)

    def run(self, request, id: str):
        def to_json(env):
            env = env.replace("'", "\"")
            return json.loads(env)
        
        try:
            app = model_to_dict(App.objects.get(id=id))
            container = client.containers.run(
                name=app['name'], image=app['image'], environment=to_json(app['environment']), command=app['command'], detach=True)
    
            return Response(container.logs(), status=status.HTTP_200_OK)
        except App.DoesNotExist as err:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except docker.errors.APIError as err:
            return Response("duplicate name for container", status=status.HTTP_409_CONFLICT)

    def actions_history(self, request):
        return Response('history')