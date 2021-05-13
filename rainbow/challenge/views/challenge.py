import datetime

from django.db.models import Q
from rest_framework import viewsets

from challenge.models import SupportChallenge
from challenge.models.challenge import Challenge, ArticleChallenge, EventParticipantChallenge
from challenge.models.challenge.event_organizer import EventOrganizerChallenge
from challenge.models.challenge.project import ProjectChallenge
from challenge.models.challenge.reacting import ReactingChallenge
from challenge.models.challenge.school_gsa import SchoolGSAChallenge
from challenge.models.challenge.story import StoryChallenge
from challenge.serializers.challenge import ChallengeSerializer, ArticleChallengeSerializer, \
    EventParticipantChallengeSerializer, SchoolGSAChallengeSerializer, EventOrganizerChallengeSerializer, \
    StoryChallengeSerializer, ProjectChallengeSerializer, ReactingChallengeSerializer, SupportChallengeSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ChallengeSerializer
    queryset = Challenge.active.all()


class ArticleChallengeViewSet(viewsets.ModelViewSet):
    """
    A viewset for Article challenges.
    """
    serializer_class = ArticleChallengeSerializer
    queryset = ArticleChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class EventParticipantChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = EventParticipantChallengeSerializer
    queryset = EventParticipantChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class SchoolGSAChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = SchoolGSAChallengeSerializer
    queryset = SchoolGSAChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class EventOrganizerChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = EventOrganizerChallengeSerializer
    queryset = EventOrganizerChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class StoryChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = StoryChallengeSerializer
    queryset = StoryChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class ProjectChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = ProjectChallengeSerializer
    queryset = ProjectChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class ReactingChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = ReactingChallengeSerializer
    queryset = ReactingChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )


class SupportChallengeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for EventParticipant challenges.
    """
    serializer_class = SupportChallengeSerializer
    queryset = SupportChallenge.objects.filter(
        Q(main_challenge__published=True),
        Q(main_challenge__start_date__lt=datetime.datetime.now()) | Q(main_challenge__start_date__isnull=True),
        Q(main_challenge__end_date__gt=datetime.datetime.now()) | Q(main_challenge__end_date__isnull=True)
    )
