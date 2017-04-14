from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Brian J. Goode'

doc = """
Sociodemographics Survey.
"""


class Constants(BaseConstants):
    name_in_url = 'survey_initial'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        verbose_name = 'What is your age?'
        )

    income = models.PositiveIntegerField(
        verbose_name = 'What is your household income?',
        choices = [
            [1, 'Less than $25,000'],
            [2, '$25,000 - $49,999'],
            [3, '$50,000 - $74,999'],
            [4, '$75,000 - $99,999'],
            [5, '$100,000 - $124,999'],
            [6, '$125,000 - $149,999'],
            [7, 'Greater than $150,000'],
        ],
    )

    sex = models.CharField(
        verbose_name = 'What is your sex?',
        choices = [
            'male',
            'female',
        ],
    )

    maritalStatus = models.PositiveIntegerField(
        verbose_name = 'What is your marital status?',
        choices = [
            [1, 'single'],
            [2, 'married'],
            [3, 'living with partner'],
        ],
    )

    country_reside = models.CharField(
        verbose_name = 'In which country do you currently reside?'
    )

    country_born = models.CharField(
        verbose_name = 'In which country were you born?'
    )

    hispanic = models.BooleanField(
        verbose_name = 'Are you Hispanic or Latino?'
    )

    race = models.PositiveIntegerField(
        verbose_name = 'What is your race?',
        choices = [
            [1, 'American Indian or Alaska Native'],
            [2, 'Asian'],
            [3, 'Black or African American'],
            [4, 'Native Hawaiian or Other Pacific Islander'],
            [5, 'White (non-Hispanic)'],
        ],
    )

    degree = models.PositiveIntegerField(
        verbose_name = 'What is your highest degree?',
        choices = [
            [1, 'Less than high school'],
            [2, 'Some High School (9-12 grades)'],
            [3, 'High School Graduate'],
            [4, 'Some College (no degree)'],
            [5, 'Associate Degree'],
            [6, 'BA/BS'],
            [7, 'JD/MA/MS/MBA/MD'],
            [8, 'PhD/Postdoc'],
        ],
    )

    major = models.CharField(
        verbose_name = '''
        What is your area of specialty/major? (e.g., Economics, 
        Engineering, Finance, Literature, History, 
        Computer Science, etc.)
        '''
    )

    subject_econ = models.BooleanField(
        verbose_name = 'Economics',
    )
    
    subject_finance = models.BooleanField(
        verbose_name = 'Finance',
    )

    subject_stat = models.BooleanField(
        verbose_name = 'Statistics',
    )

    occupation = models.CharField(
        verbose_name = 'What is your occupation?'
    )
  

