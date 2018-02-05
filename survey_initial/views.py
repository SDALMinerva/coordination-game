from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class SocioDemographic(Page):
    form_model = models.Player
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
    form_model = models.Player
    form_fields = [
        "daringness",
        "selflessness",
        "trustingness",
        "donation",
        "punishInclination",
    ]
    
class Behavioral2(Page):
    form_model = models.Player
    form_fields = ['timeScenerio_{}'.format(i) for i in range(1, 26)]
    
    def vars_for_template(self):
        return {'sixMonthOffers': [
                {"num": 1, "amt": 100},
                {"num": 2, "amt": 103},
                {"num": 3, "amt": 106.10},
                {"num": 4, "amt": 109.20},
                {"num": 5, "amt": 112.40},
                {"num": 6, "amt": 115.60},
                {"num": 7, "amt": 118.80},
                {"num": 8, "amt": 122.10},
                {"num": 9, "amt": 125.40},
                {"num": 10, "amt": 128.80},
                {"num": 11, "amt": 132.30},
                {"num": 12, "amt": 135.70},
                {"num": 13, "amt": 139.20},
                {"num": 14, "amt": 142.80},
                {"num": 15, "amt": 146.40},
                {"num": 16, "amt": 150.10},
                {"num": 17, "amt": 153.80},
                {"num": 18, "amt": 157.50},
                {"num": 19, "amt": 161.30},
                {"num": 20, "amt": 165.10},
                {"num": 21, "amt": 169.00},
                {"num": 22, "amt": 172.90},
                {"num": 23, "amt": 176.90},
                {"num": 24, "amt": 180.90},
                {"num": 25, "amt": 185.00},
            ]
        }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    SocioDemographic,
    Behavioral1,
    Behavioral2,
    Results,
]
