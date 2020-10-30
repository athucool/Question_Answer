from .serializers import AnswerSerializers,QuestionSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError 
from rest_framework.response import Response
from .permissions import ISAuthorOrReadOnly
from rest_framework import viewsets,generics,status
from questions.models import Question,Answer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import response

from rest_framework.views import APIView

class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    lookup_field ="slug"
    serializer_class=QuestionSerializer
    permission_class=[IsAuthenticated,ISAuthorOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

class AnswerCreateViewSet(generics.CreateAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializers
    permission_class=[IsAuthenticated]
    def perform_create(self,serializer):
        request_user=self.request.user
        kwarg_slug=self.kwargs.get("slug")
        question=get_object_or_404(Question,slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("you alreay gave answer..!")
        serializer.save(author=request_user,question=question)    

class AnswerListApiView(generics.ListAPIView):
    serializer_class=AnswerSerializers
    permission_class=[IsAuthenticated]
    def get_queryset(self):
        kwarg_slug=self.kwargs.get("slug")
        m=Answer.objects.filter(question__slug=kwarg_slug).order_by("created_at")
        return  Answer.objects.filter(question__slug=kwarg_slug).order_by("created_at")
    

class AnswerupdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializers
    permission_class=[IsAuthenticated,ISAuthorOrReadOnly]
    def put(self, request, *args, **kwargs):
        return "{self.update(request, *args, **kwargs)--{}}".format(self.request.data)

        
class AnswerlikeApiView(APIView):
    serializer_class=AnswerSerializers
    permission_class=[IsAuthenticated]

    def post(self,request,pk):
        answer=get_object_or_404(Answer,pk=pk)
        user=request.user
        answer.voters.add(user)
        answer.save()

        serializer_context={"request":request}
        serializer=self.serializer_class(answer,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    def delete(self,request,pk):
        answer=get_object_or_404(Answer,pk=pk)
        user=request.user
        answer.voters.remove(user)
        answer.save()

        serializer_context={"request":request}
        serializer=self.serializer_class(answer,context=serializer_context)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
           