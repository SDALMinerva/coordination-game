from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    cases = [
                "no_specify", 
#                "tribe", 
#                "other_asian", 
#                "other_islander",
#                "other_race", 
#                "other_work", 
#                "other_freetime",
                ]
    
    def play_round(self):
        ans = {
            "lastName": "Washington",
            "firstName": "George",
            "middleInitial": "F",
            "age": 67,
            "sexBirth": "Male",
            "sexCurrent": "Male",
            "ethnicity": "English",
            "race": 1,
            "tribe": None,
            "otherAsian": None,
            "otherPacificIslander": None,
            "otherRace": None,
            "maritalStatus": 2,
            "country_born": "UK - United Kingdom",
            "country_reside": "US - United States",
            "province_reside": "Virginia",
            "city_reside": "Mount Vernon",
            "reside_len": 20,
            "socialContact": 7,
            "degree": 1,
            "major": 17,
            "income": 5,
            "subject_econ": False,
            "subject_finance": False,
            "subject_stat": False,
            "partTime": False,
            "fullTime": False,
            "homeEmployed": False,
            "homemaker": False,
            "fullTimeStudent": False,
            "partTimeStudent": False,
            "selfEmployed": False,
            "lookingWork": False,
            "notLookingWork": False,
            "military": False,
            "retired": True,
            "unableWork": False,
            "otherWork": False,
            "otherWorkSpecify": None,
            "sports": False,
            "performingArts": True,
            "music": False,
            "volunteer": True,
            "hobby": False,
            "otherFreeTime": False,
            "otherFreeTimeSpecify": None,
            "occupation": "Former President",
            "income": 5,
            "numRoommates": 7,

# Those entried commented out depend on whether student or not.
#            "residents0to6": 0,
#            "residents7to12": 1,
#            "residents13to18": 0,
#            "residents19to65": 4,
#            "residents65up": 2,
#            "activitySchool": 2,
#            "activityAfterSchool": 1,
#            "activityGroup": 0,
            "activitySports": 0,
            "activityFlu": 0,
#            "activityWork": 1,
            "activityPubTrans": 0,
#            "activityEvening": 0,
            "activityCollegeClubs": 1,
            "activityPartTimeWork": 1,
        }
        if self.case == "no_specify":
            yield (pages.SocioDemographic, ans)
            yield (pages.Results)

# Check these if statements...            
"""
        elif self.case == "tribe":
            ans["race"] = 3
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["tribe"] = "Cherokee"
            yield (pages.SocioDemographic, ans)
        elif self.case == "other_asian":
            ans["race"] = 13
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["otherAsian"] = "Cambodian"
            yield (pages.SocioDemographic, ans)
        elif self.case == "other_islander":
            ans["race"] = 14
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["otherPacificIslander"] = "Indonesian"
            yield (pages.SocioDemographic, ans)
        elif self.case == "other_race":
            ans["race"] = 15
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["otherRace"] = "Afghan"
            yield (pages.SocioDemographic, ans)
        elif self.case == "other_work":
            ans["otherWork"] = True
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["otherWorkSpecify"] = "Public Office"
            yield (pages.SocioDemographic, ans)
        elif self.case == "other_freetime":
            ans["otherFreeTime"] = True
            yield SubmissionMustFail (pages.SocioDemographic, ans)
            ans["otherFreeTimeSpecify"] = "Ride horses"
            yield (pages.SocioDemographic, ans)
        yield (pages.Results)
"""
