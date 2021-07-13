from django.contrib import admin

from challenge.models import Challenge, ArticleChallenge, EventParticipantChallenge, SupportChallenge

from challenge.models.event_organizer import EventOrganizerChallenge
from challenge.models.project import ProjectChallenge
from challenge.models.reacting import ReactingChallenge
from challenge.models.school_gsa import SchoolGSAChallenge
from challenge.models.story import StoryChallenge
from results.models.prize import ClaimedPrize

# Challenges
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'points', 'region', 'published', 'start_date', 'end_date')
    list_filter = ('type', 'region', 'published', )

class ArticleChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class EventParticipantChallengeAdmin(admin.ModelAdmin):
    list_display = ('event_name', )

class SchoolGSAChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class EventOrganizerChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class StoryChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class ProjectChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class ReactingChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', )

class SupportChallengeAdmin(admin.ModelAdmin):
    list_display = ('main_challenge', 'organization', )






admin.site.register(Challenge, ChallengeAdmin)

# challenge
admin.site.register(ArticleChallenge, ArticleChallengeAdmin)
admin.site.register(EventParticipantChallenge, EventParticipantChallengeAdmin)
admin.site.register(SchoolGSAChallenge, SchoolGSAChallengeAdmin)
admin.site.register(EventOrganizerChallenge, EventOrganizerChallengeAdmin)
admin.site.register(StoryChallenge, StoryChallengeAdmin)
admin.site.register(ProjectChallenge, ProjectChallengeAdmin)
admin.site.register(ReactingChallenge, ReactingChallengeAdmin)
admin.site.register(SupportChallenge, SupportChallengeAdmin)


