from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    template_name = "survey_initial/intro.html"
    
class SocioDemographic(Page):
    form_model = 'player'
    def get_form_fields(self):
        questions = [
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
        ]
        if self.session.config['student_survey']:
            questions.extend([
                "numRoommates",
                "activityCollegeClubs",
                "activityPartTimeWork",
                "activityPubTrans",
                "activitySports",
                "activityFlu",])
        else:
            questions.extend([
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
                "activityEvening",])
        return questions


class Behavioral1(Page):
    form_model = 'player'
    form_fields = [
        "daringness",
        "selflessness",
        "trustingness",
        "donation",
        "punishInclination",
    ]


class Behavioral2(Page):
    form_model = 'player'
    form_fields = ['timeScenerio_{}'.format(i) for i in range(1, 26)]


class Behavioral3(Page):
    form_model = 'player'
    form_fields = ['coinScenerio_{}'.format(i) for i in range(1, 32)]
    
    def vars_for_template(self):
        return {'coinOffers': [{"num": i, "amt": 10 * (i - 1)} for i in range(1, 32)]}

    
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Intro,
    SocioDemographic,
    Behavioral1,
    Behavioral2,
    Behavioral3,
    Results,
]
