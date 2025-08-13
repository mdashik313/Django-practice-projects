from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_app.serializers import StudentSerializer
from drf_app.models import Student


class TestView(APIView):

    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        # data = {
        #     'username': 'admin',
        #     'years_active': 10
        # }

        # return Response(data)

        query_set = Student.objects.all()

        # student1 = query_set.first()
        # serializer = StudentSerializer(student1)

        serializer = StudentSerializer(query_set, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)