from rest_framework import serializers

from challenge.models import SupportChallenge, ArticleChallenge, EventParticipantChallenge
from challenge.models.base import Challenge
from challenge.models.custom import CustomChallenge
from challenge.models.event_organizer import EventOrganizerChallenge
from challenge.models.project import ProjectChallenge
from challenge.models.quiz import QuizChallenge
from challenge.models.reacting import ReactingChallenge
from challenge.models.school_gsa import SchoolGSAChallenge
from challenge.models.story import StoryChallenge
from joined_challenge.models import JoinedChallenge


class ChallengeSerializer(serializers.ModelSerializer):
    concrete_challenge_uuid = serializers.UUIDField()
    can_be_joined = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = ('uuid',
                  'type',
                  'name',
                  'description',
                  'image',
                  'points',
                  'region',
                  'start_date',
                  'end_date',
                  'multiple',
                  'needs_confirmation',
                  'concrete_challenge_uuid',
                  'can_be_joined'
                  )

    def get_can_be_joined(self, obj):
        """
        Checks if the current user can join this challenge
        Users can't join challenges which are not multiple and they have already joined it.
        """
        if obj.multiple is False:
            user = self.context["request"].user
            joined_challenge = JoinedChallenge.objects.filter(challenge=obj, user=user)
            if len(joined_challenge) > 0:
                return False
            return True
        return True


class BaseChallengeSerializer(serializers.ModelSerializer):
    main_challenge = ChallengeSerializer()


class ArticleChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = ArticleChallenge
        fields = '__all__'


class EventParticipantChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = EventParticipantChallenge
        fields = '__all__'


class SchoolGSAChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = SchoolGSAChallenge
        fields = '__all__'


class EventOrganizerChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = EventOrganizerChallenge
        fields = '__all__'


class StoryChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = StoryChallenge
        fields = '__all__'


class ProjectChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = ProjectChallenge
        fields = '__all__'


class ReactingChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = ReactingChallenge
        fields = '__all__'


class SupportChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = SupportChallenge
        fields = '__all__'


class QuizChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = QuizChallenge
        fields = '__all__'


class CustomChallengeSerializer(BaseChallengeSerializer):

    class Meta:
        model = CustomChallenge
        fields = '__all__'
