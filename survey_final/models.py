from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey_final'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Question 13
#    q13a_transportation = models.CharField(
#        verbose_name = "Used public transportation",
#        choices = [
#            'Never',
#            'Once a year',
#            'A couple of times a year',
#            'A few times a month',
#            '1-2 times a week',
#            'A couple of times a week',
#            'Once a day',
#            'More than once a day',        
#        ],
#        widget = widgets.RadioSelectHorizontal(),    
#    )
   q13b_volunteer = models.CharField(
       verbose_name = "Performed volunteer work",
       choices = [
           'Never',
           'Once a year',
           'A couple of times a year',
           'A few times a month',
           '1-2 times a week',
           'A couple of times a week',
          'Once a day',
           'More than once a day',      
      ],
       widget = widgets.RadioSelectHorizontal(),    
    )
    q13c_donations = models.CharField(
        verbose_name = "Helped raise donations (e.g., money, books) for a cause or campaign",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',       
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q13d_discussPolitics = models.CharField(
        verbose_name = "Discussed politics",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',        
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q13e_communicate = models.CharField(
        verbose_name = "Publicly communicated your opinion about a cause (e.g., blog, email, petition)",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',     
        ],
        widget = widgets.RadioSelectHorizontal(),            
    )
    q13f_demonstrate = models.CharField(
        verbose_name = "Demonstrated for a cause (e.g., boycott, rally, protest)",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',       
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q13g_elections = models.CharField(
        verbose_name = "Voted in elections",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',        
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q13h_risk = models.CharField(
        verbose_name = "Taken a risk because you feel you have more to gain",
        choices = [
            'Never',
            'Once a year',
            'A couple of times a year',
            'A few times a month',
            '1-2 times a week',
            'A couple of times a week',
            'Once a day',
            'More than once a day',       
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    
    # Question 14
    ## Added Programmatically Below.
    q14_l_networking_otherPrint = models.CharField(
        blank = True    
    )

    # Question 15
    q15a_ethics_wealth = models.CharField(
        verbose_name = "Wealthy people should pay a larger share of taxes than they do now",
        choices = [
            'Prefer not to answer',
            'No Opinion',
            'Srongly Disagree',
            'Disagree Somewhat',
            'Indifferent',
            'Agree Somewhat',
            'Strongly Agree',        
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q15b_ethics_climate = models.CharField(
        verbose_name = "Addressing global climate change should be a federal priority",
        choices = [
            'Prefer not to answer',
            'No Opinion',
            'Srongly Disagree',
            'Disagree Somewhat',
            'Indifferent',
            'Agree Somewhat',
            'Strongly Agree',        
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q15c_ethics_gunControl = models.CharField(
        verbose_name = "The federal government should have stricter gun control laws",
        choices = [
            'Prefer not to answer',
            'No Opinion',
            'Srongly Disagree',
            'Disagree Somewhat',
            'Indifferent',
            'Agree Somewhat',
            'Strongly Agree',        
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
#    q15d_ethics_admissions = models.CharField(
#        verbose_name = "Affirmative action in college admissions should be abolished",
#        choices = [
#            'Srongly Disagree',
#            'Disagree Somewhat',
#            'Indifferent',
#            'Agree Somewhat',
#            'Strongly Agree',
#            'No Opinion',
#            'Prefer not to answer',        
#        ],
#        widget = widgets.RadioSelectHorizontal(),
#    )
#    q15e_ethics_taxes = models.CharField(
#        verbose_name = "The federal government should raise taxes to reduce the deficit",
#        choices = [
#            'Srongly Disagree',
#            'Disagree Somewhat',
#            'Indifferent',
#            'Agree Somewhat',
#            'Strongly Agree',
#            'No Opinion',
#            'Prefer not to answer',        
#        ],
#        widget = widgets.RadioSelectHorizontal(),
#    )
   
    
    # start behavioral questions
    # start preference elicitation
    daringness = models.PositiveIntegerField(
        verbose_name = "How do you see yourself? Are you a person who is generally willing to take risks, or do you try to avoid taking risks? Please indicate your answer on a scale from 0 to 10, where a 0 means \"not at all willing to take risks\", and a 10 means \"very willing to take risks\". You can also use the values in between to indicate where you fall on the scale.",
        choices = [
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10"],
        ],
        widget = widgets.RadioSelectHorizontal,
    )
    
    risky_project = models.PositiveIntegerField(
        verbose_name = "How do you see yourself? In comparison to others are you a person who is generally willing to give up something today in order to benefit from that in the future, or are you not willing to do so in comparison to others? Please indicate your answer on a scale from 0 to 10, where a 0 means \"not at all willing to give up something\", and a 10 means \"very willing to give up something\". You can use the values in between to indicate where you fall on the scale.",
        min=0, 
        max=100,
    )
    
    risky_project_outcome = models.BooleanField(blank=True)
    
    risky_project_2 = models.PositiveIntegerField(
        verbose_name = "How do you see yourself? In comparison to others are you a person who is generally willing to give up something today in order to benefit from that in the future, or are you not willing to do so in comparison to others? Please indicate your answer on a scale from 0 to 10, where a 0 means \"not at all willing to give up something\", and a 10 means \"very willing to give up something\". You can use the values in between to indicate where you fall on the scale.",
        min=0, 
        max=100,
    )
    
    risky_project_outcome_2 = models.BooleanField(blank=True)
    
    # end preference elicitation
    
    # start preference module ii
    coinScenerio_1 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "0$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_2 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "10$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_3 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "20$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_4 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "30$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_5 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "40$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_6 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "50$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_7 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "60$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_8 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "70$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_9 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "80$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_10 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "90$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_11 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "100$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_12 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "110$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_13 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "120$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_14 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "130$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_15 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "140$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_16 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "150$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_17 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "160$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_18 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "170$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_19 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "180$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_20 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "190$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_21 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "200$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_22 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "210$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_23 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "220$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_24 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "230$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_25 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "240$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_26 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "250$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_27 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "260$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_28 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "270$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_29 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "280$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_30 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "290$"],
        ],
        widget = widgets.RadioSelect,
    )

    coinScenerio_31 = models.PositiveIntegerField(
        choices = [
            [1, "Tail = 300$    Head = 0$"],
            [2, "300$"],
        ],
        widget = widgets.RadioSelect,
    )
    # end preference module ii


columns = [
            'Facebook',
            'Twitter',
            'LinkedIn',
            'Instagram',
            'Reddit',
            'WhatsApp',
            'Meetup',
            'Nextdoor',
            'Snapchat',
            'Weibo',
            'WeChat',        
        ]
        
rows = [
    ("prof_network", "Professional networking"),
    ("soc_network", "Social networking"),
    ("xchng_info", "Exchange of information with peers and family"),
    ("soc_events","Organize and/or attend social events"),
    ("pol_events","Organize and/or attend political events"),
    ("news_info", "News and information about people and places"),
    ("job", "Job seeking"),
    ("money", "To make money"),
    ("games", "To play games"),
    ("research", "Research"),
#    ("other", "Other"),
#    ("dont_use","I don’t use this social networking site"),
]

i = 0
for r in rows:
    for c in columns:
        i += 1
        field_name = 'q14_{}_{}X{}'.format(i, r[0], c)    
        Player.add_to_class(field_name, models.BooleanField(
            verbose_name = r[1],
            widget = widgets.CheckboxInput(),
        ))

