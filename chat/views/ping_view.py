from django.shortcuts import redirect
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    def get(self, _: Request) -> Response:
        return redirect('https://fr-mm.github.io/saltzapp/')
