from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class AppViewSet(ViewSet):
    def create(self, request):
        return Response('create')
    def list(self, request):
        return Response('list')
    def get(self, request, id):
        return Response('get ' + id)

    def delete(self, request):
        return Response('delete')

    def edit(self, request):
        return Response('edit')

    def run(self, request):
        return Response('run')

    def actionsHistory(self, request):
        return Response('history')