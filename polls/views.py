from typing import Generic
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from authorization.backends import JWTAuthentication
from polls.models import Poll
from polls.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def poll_vote(request):
    if request.method == "POST":
        user = request.user
        poll_id = request.POST.get("poll")
        candidate_id = request.POST.get("candidate")

        if candidate_id and poll_id:
            candidate = Candidate.objects.filter(id=candidate_id).first()
            poll = Poll.objects.filter(id=poll_id).first()
            vote,created = Election.objects.get_or_create(poll=poll,user=user,candidate=candidate,vote=1)
            if created:
                vote.save()
            else:
                vote.delete()
            
            return Response(PollSerializer(poll).data,status=status.HTTP_200_OK)
        else:
            raise exceptions.ValidationError("Candidate Key and Poll id is required")

        


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def polls(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def poll_detail(request,pk):
    poll = Poll.objects.filter(pk=pk).first()
    serializer = PollSerializer(poll)
    return Response(serializer.data,status=status.HTTP_200_OK)
