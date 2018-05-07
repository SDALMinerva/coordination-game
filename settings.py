import os
import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = environ.Path(__file__) - 1
env = environ.Env()
env.read_env(ROOT_DIR('.env'))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if env.str('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = env.str('OTREE_ADMIN_PASSWORD', None)

# don't share this with anybody.
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

possible_hosts = env.str('DJANGO_ALLOWED_HOST', None)
ALLOWED_HOSTS = possible_hosts.split(',') if possible_hosts is not None else []

SENTRY_DSN = 'http://9f3361069ae443dea470f6832c7ed799:10c67778bcea42428cb51b2cff9fd033@sentry.otree.org/317'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = env.str('OTREE_AUTH_LEVEL', None)

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY', None)


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = [
    'otree',
    'avatar',
    'network',
    'practice_network',
    'clicktracking',
    'django_extensions',
]

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
Available Apps
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    # AMT Configs
    'real_world_currency_per_point': 0.1,
    'participation_fee': 7.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
    
    # Narrative Configs
    'thresholds': '1,3',
    'show_network_threshold': 'False',
    'messages': 'I will participate./I will not participate.',

    # Payoff Configs
    'payoff_no_participate': '50',
    'payoff_below_threshold': '0',
    'payoff_above_threshold': '100',
    'payoff_round': '1',
    
    # Survey Type
    'student_survey': 'True',

    # Messaging Type
    'instant_messaging': 'False',               #True, False
}

sequence = [
    'welcome_consent',
    'survey_initial', 
    'instructions',
    'practice',
    'main',
    'survey_final',
]

DEV_CONFIGS = [
     {
         'name': 'run_group3_treatment1',
         'display_name': '[1] Run: Groups, 3; Messaging, none; Network Knowledge, local',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'none',               #none, wall, bilateral, both
          'condition_network_knowledge': 'local',      #local, global
     },
     {
         'name': 'run_group3_treatment3',
         'display_name': '[3] Run: Groups, 3; Messaging, bilateral; Network Knowledge, local',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'bilateral',           #none, wall, bilateral, both
          'condition_network_knowledge': 'local',      #local, global
     },
     {
         'name': 'run_group3_treatment4',
         'display_name': '[4] Run: Groups, 3; Messaging, both; Network Knowledge, local',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'both',               #none, wall, bilateral, both
          'condition_network_knowledge': 'local',      #local, global
     },
     {
         'name': 'run_group3_treatment5',
         'display_name': '[5] Run: Groups, 3; Messaging, none; Network Knowledge, global',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'none',               #none, wall, bilateral, both
          'condition_network_knowledge': 'global',      #local, global
     },
     {
         'name': 'run_group3_treatment7',
         'display_name': '[7] Run: Groups, 3; Messaging, bilateral; Network Knowledge, global',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'bilateral',               #none, wall, bilateral, both
          'condition_network_knowledge': 'global',      #local, global
     },
     {
         'name': 'run_group3_treatment8',
         'display_name': '[8] Run: Groups, 3; Messaging, both; Network Knowledge, global',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'both',               #none, wall, bilateral, both
          'condition_network_knowledge': 'global',      #local, global
     },
]

SESSION_CONFIGS = [
     {
         'name': 'run_group3_treatment2',
         'display_name': '[2] Run: Groups, 3; Messaging, wall; Network Knowledge, local',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'wall',               #none, wall, bilateral, both
          'condition_network_knowledge': 'local',      #local, global
     },
     {
         'name': 'run_group3_treatment6',
         'display_name': '[6] Run: Groups, 3; Messaging, wall; Network Knowledge, global',
         'num_demo_participants': 1,
         'app_sequence': sequence,
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'wall',               #none, wall, bilateral, both
          'condition_network_knowledge': 'global',      #local, global
     },
     {
         'name': 'test_welcome',
         'display_name': 'Test: Welcome and Consent',
         'num_demo_participants': 1,
         'app_sequence': [
                          'welcome_consent', 
                         ],
     },
     {
         'name': 'test_instructions',
         'display_name': 'Test: Instructions',
         'num_demo_participants': 1,
         'app_sequence': [
                          'instructions', 
                         ],
         'condition_messaging': 'wall',
         'condition_network_knowledge': 'local',
     },
     {
         'name': 'test_practice',
         'display_name': 'Test: Practice',
         'num_demo_participants': 5,
         'app_sequence': [
                          'practice', 
                         ],
         'condition_messaging': 'wall',
         'condition_network_knowledge': 'global',
     },
     {
         'name': 'test_survey_initial',
         'display_name': 'Test: Initial Survey',
         'num_demo_participants': 1,
         'app_sequence': [ 
                          'survey_initial',
                         ],
     },
     {
         'name': 'test_main',
         'display_name': 'Test: Main Coordination Experiment',
         'num_demo_participants': 15,
         'app_sequence': [ 
                          'main',
                         ],
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'bilateral',               #none, wall, bilateral, both
          'condition_network_knowledge': 'global',      #local, global
     },
     {
         'name': 'test_main_oneParticipant',
         'display_name': 'Test: Main Coordination Experiment',
         'num_demo_participants': 1,
         'app_sequence': [ 
                          'main',
                         ],
          # Rounds
          'round_seq_file': 'seq-48rounds.json',
          
          # Treatment Configs
          'condition_messaging': 'wall',               #none, wall, bilateral, both
          'condition_network_knowledge': 'local',      #local, global
     },
     {
         'name': 'test_survey_final',
         'display_name': 'Test: Final Survey',
         'num_demo_participants': 1,
         'app_sequence': [
                          'survey_final',
                         ],
     },
]

ROOMS = [
    {
        'name': 'lab',
        'display_name': 'In-Person Room (15 Participants)',
        'participant_label_file': '15Participants.txt',
    },
]

if DEBUG:
    SESSION_CONFIGS += DEV_CONFIGS

CHANNEL_ROUTING = 'routing.channel_routing'

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
