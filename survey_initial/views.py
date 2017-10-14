from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SocioDemographic(Page):
    form_model = models.Player
    form_fields = [
        'age',
        'skipAgeQ',
        'sex',
        'income',
        'numRoommates',
        'maritalStatus',
        'socialContact',
        'country_born',
        'country_reside',
        'city',
        'skipCityQ',
        'neighborhoodType',
        'ethnicity',
        'degree',
        'major',
        'subject_econ',
        'subject_finance',
        'subject_stat',
        'skipSubjectQ',
        'partTime',    
        'fullTime',
        'homeEmployed',
        'homemaker',
        'fullTimeStudent',
        'partTimeStudent',
        'selfEmployed',
        'lookingWork',
        'notLookingWork',
        'student',
        'military',
        'retired',
        'unableWork',
        'otherWork',
        'skipWorkQ',
        'sports',
        'performingArts',
        'music',
        'volunteer',
        'hobby',
        'otherFreeTime',
        'skipFreeTimeQ',
        'occupation',
        'skipOccupationQ',
        'residents0to6',
        'residents7to12',
        'residents13to18',
        'residents19to65',
        'residents65up',
        'skipResidentsQ',
        'activity18School',
        'activity18AfterSchool',
        'activity18Group',
        'activity18Sports',
        'activity18Flu',
        'skipActivity18Q',
        'activity19Work',
        'activity19School',
        'activity19PublicTrans',
        'activity19Group',
        'activity19Sports',
        'activity19Flu',
        'skipActivity19Q',
    ]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    SocioDemographic,
    ResultsWaitPage,
    Results
]
