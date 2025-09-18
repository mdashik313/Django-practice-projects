from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import StudentSerializer
from .models import Student


class TestView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]

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
    
    # def put(self, request, id):
    #     name = request.data.get('name')
    #     student = Student.objects.filter(id=id).filter()

    #     if student is None:
    #         response_data = {
    #             'response': "Student doesn't exist"
    #         }

    #         return Response(response_data)
        
    #     student.name = name 
    #     student.save()

    #     serializer = StudentSerializer(student)

    #     response_data = {
    #         'response': "Student updated",
    #         'data': serializer.data 
    #     }

    #     return Response(response_data)