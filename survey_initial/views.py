from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SocioDemographic(Page):
    form_model = models.Player
    form_fields = [
        "lastName",
        "firstName",
        "middleInitial",
        "age",
        "sexBirth",
        "sexCurrent",
        "ethnicity",
        "race",
        "tribe",
        "otherAsian",
        "otherPacificIslander",
        "otherRace",
        "maritalStatus",
        "country_born",
        "country_reside",
        "province_reside",
        "city_reside",
        "reside_len",
        "socialContact",
        "degree",
        "major",
        "income",
        "subject_econ",
        "subject_finance",
        "subject_stat",
        "numRoommates",
        "partTime",    
        "fullTime",
        "homeEmployed",
        "homemaker",
        "fullTimeStudent",
        "partTimeStudent",
        "selfEmployed",
        "lookingWork",
        "notLookingWork",
        "military",
        "retired",
        "unableWork",
        "otherWork",
        "otherWorkSpecify",
        "sports",
        "performingArts",
        "music",
        "volunteer",
        "hobby",
        "otherFreeTime",
        "otherFreeTimeSpecify",
        "occupation",
        "income",
        "numRoommates",
        "residents0to6",
        "residents7to12",
        "residents13to18",
        "residents19to65",
        "residents65up",
        "activitySchool",
        "activityAfterSchool",
        "activityGroup",
        "activitySports",
        "activityFlu",
        "activityWork",
        "activityPubTrans",
        "activityEvening",
    ]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    SocioDemographic,
    Results,
]
