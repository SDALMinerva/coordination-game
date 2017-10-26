from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Brian J. Goode & Ethan Vu'

doc = """
Sociodemographics Survey.
"""


class Constants(BaseConstants):
    name_in_url = 'survey_initial'
    players_per_group = None
    num_rounds = 1
    countries = [
        'Skip this question',
        'AD - Andorra',
        'AE - United Arab Emirates',
        'AF - Afghanistan',
        'AG - Antigua and Barbuda',
        'AI - Anguilla',
        'AL - Albania',
        'AM - Armenia',
        'AO - Angola',
        'AQ - Antarctica',
        'AR - Argentina',
        'AS - American Samoa',
        'AT - Austria',
        'AU - Australia',
        'AW - Aruba',
        'AZ - Azerbaijan',
        'BA - Bosnia and Herzegovina',
        'BB - Barbados',
        'BD - Bangladesh',
        'BE - Belgium',
        'BF - Burkina Faso',
        'BG - Bulgaria',
        'BH - Bahrain',
        'BI - Burundi',
        'BJ - Benin',
        'BL - Saint Barthelemy',
        'BM - Bermuda',
        'BN - Brunei',
        'BO - Bolivia',
        'BR - Brazil',
        'BS - Bahamas, The',
        'BT - Bhutan',
        'BV - Bouvet Island',
        'BW - Botswana',
        'BY - Belarus',
        'BZ - Belize',
        'CA - Canada',
        'CC - Cocos (Keeling) Islands',
        'CD - Congo, Democratic Republic of the',
        'CF - Central African Republic',
        'CG - Congo, Republic of the',
        'CH - Switzerland',
        'CI - Cote d\'Ivoire',
        'CK - Cook Islands',
        'CL - Chile',
        'CM - Cameroon',
        'CN - China',
        'CO - Colombia',
        'CR - Costa Rica',
        'CU - Cuba',
        'CV - Cape Verde',
        'CW - Curacao',
        'CX - Christmas Island',
        'CY - Cyprus',
        'CZ - Czech Republic',
        'DE - Germany',
        'DJ - Djibouti',
        'DK - Denmark',
        'DM - Dominica',
        'DO - Dominican Republic',
        'DZ - Algeria',
        'EC - Ecuador',
        'EE - Estonia',
        'EG - Egypt',
        'EH - Western Sahara',
        'ER - Eritrea',
        'ES - Spain',
        'ET - Ethiopia',
        'FI - Finland',
        'FJ - Fiji',
        'FK - Falkland Islands (Islas Malvinas)',
        'FM - Micronesia, Federated States of',
        'FO - Faroe Islands',
        'FR - France',
        'FX - France, Metropolitan',
        'GA - Gabon',
        'GD - Grenada',
        'GE - Georgia',
        'GF - French Guiana',
        'GG - Guernsey',
        'GH - Ghana',
        'GI - Gibraltar',
        'GL - Greenland',
        'GM - Gambia, The',
        'GN - Guinea',
        'GP - Guadeloupe',
        'GQ - Equatorial Guinea',
        'GR - Greece',
        'GS - South Georgia and the Islands',
        'GT - Guatemala',
        'GU - Guam',
        'GW - Guinea-Bissau',
        'GY - Guyana',
        'HK - Hong Kong',
        'HM - Heard Island and McDonald Islands',
        'HN - Honduras',
        'HR - Croatia',
        'HT - Haiti',
        'HU - Hungary',
        'ID - Indonesia',
        'IE - Ireland',
        'IL - Israel',
        'IM - Isle of Man',
        'IN - India',
        'IO - British Indian Ocean Territory',
        'IQ - Iraq',
        'IR - Iran',
        'IS - Iceland',
        'IT - Italy',
        'JE - Jersey',
        'JM - Jamaica',
        'JO - Jordan',
        'JP - Japan',
        'KE - Kenya',
        'KG - Kyrgyzstan',
        'KH - Cambodia',
        'KI - Kiribati',
        'KM - Comoros',
        'KN - Saint Kitts and Nevis',
        'KP - Korea, North',
        'KR - Korea, South',
        'KW - Kuwait',
        'KY - Cayman Islands',
        'KZ - Kazakhstan',
        'LA - Laos',
        'LB - Lebanon',
        'LC - Saint Lucia',
        'LI - Liechtenstein',
        'LK - Sri Lanka',
        'LR - Liberia',
        'LS - Lesotho',
        'LT - Lithuania',
        'LU - Luxembourg',
        'LV - Latvia',
        'LY - Libya',
        'MA - Morocco',
        'MC - Monaco',
        'MD - Moldova',
        'ME - Montenegro',
        'MF - Saint Martin',
        'MG - Madagascar',
        'MH - Marshall Islands',
        'MK - Macedonia',
        'ML - Mali',
        'MM - Burma',
        'MN - Mongolia',
        'MO - Macau',
        'MP - Northern Mariana Islands',
        'MQ - Martinique',
        'MR - Mauritania',
        'MS - Montserrat',
        'MT - Malta',
        'MU - Mauritius',
        'MV - Maldives',
        'MW - Malawi',
        'MX - Mexico',
        'MY - Malaysia',
        'MZ - Mozambique',
        'NA - Namibia',
        'NC - New Caledonia',
        'NE - Niger',
        'NF - Norfolk Island',
        'NG - Nigeria',
        'NI - Nicaragua',
        'NL - Netherlands',
        'NO - Norway',
        'NP - Nepal',
        'NR - Nauru',
        'NU - Niue',
        'NZ - New Zealand',
        'OM - Oman',
        'PA - Panama',
        'PE - Peru',
        'PF - French Polynesia',
        'PG - Papua New Guinea',
        'PH - Philippines',
        'PK - Pakistan',
        'PL - Poland',
        'PM - Saint Pierre and Miquelon',
        'PN - Pitcairn Islands',
        'PR - Puerto Rico',
        'PS - Gaza Strip',
        'PS - West Bank',
        'PT - Portugal',
        'PW - Palau',
        'PY - Paraguay',
        'QA - Qatar',
        'RE - Reunion',
        'RO - Romania',
        'RS - Serbia',
        'RU - Russia',
        'RW - Rwanda',
        'SA - Saudi Arabia',
        'SB - Solomon Islands',
        'SC - Seychelles',
        'SD - Sudan',
        'SE - Sweden',
        'SG - Singapore',
        'SH - Saint Helena, Ascension, and Tristan da Cunha',
        'SI - Slovenia',
        'SJ - Svalbard',
        'SK - Slovakia',
        'SL - Sierra Leone',
        'SM - San Marino',
        'SN - Senegal',
        'SO - Somalia',
        'SR - Suriname',
        'SS - South Sudan',
        'ST - Sao Tome and Principe',
        'SV - El Salvador',
        'SX - Sint Maarten',
        'SY - Syria',
        'SZ - Swaziland',
        'TC - Turks and Caicos Islands',
        'TD - Chad',
        'TF - French Southern and Antarctic Lands',
        'TG - Togo',
        'TH - Thailand',
        'TJ - Tajikistan',
        'TK - Tokelau',
        'TL - Timor-Leste',
        'TM - Turkmenistan',
        'TN - Tunisia',
        'TO - Tonga',
        'TR - Turkey',
        'TT - Trinidad and Tobago',
        'TV - Tuvalu',
        'TW - Taiwan',
        'TZ - Tanzania',
        'UA - Ukraine',
        'UG - Uganda',
        'UM - United States Minor Outlying Islands',
        'UK - United Kingdom',
        'US - United States',
        'UY - Uruguay',
        'UZ - Uzbekistan',
        'VA - Holy See (Vatican City)',
        'VC - Saint Vincent and the Grenadines',
        'VE - Venezuela',
        'VG - British Virgin Islands',
        'VI - Virgin Islands',
        'VN - Vietnam',
        'VU - Vanuatu',
        'WF - Wallis and Futuna',
        'WS - Samoa',
        'XK - Kosovo',
        'YE - Yemen',
        'YT - Mayotte',
        'ZA - South Africa',
        'ZM - Zambia',
        'ZW - Zimbabwe',
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        verbose_name = 'What is your age?',
        blank = True,
    )
    
    skipAgeQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )

    sex = models.CharField(
        verbose_name = 'What is your sex?',
        choices = [
            'male',
            'female',
            'Skip this question',
        ],
    )

    income = models.PositiveIntegerField(
        verbose_name = 'What is your household income [answer either in annual or monthly terms, whichever is most convenient] (answer in USD; conversion tool: https://www.google.com/finance/converter)?',
        choices = [
            [1, 'Less than $25,000'],
            [2, '$25,000 - $49,999'],
            [3, '$50,000 - $74,999'],
            [4, '$75,000 - $99,999'],
            [5, '$100,000 - $124,999'],
            [6, '$125,000 - $149,999'],
            [7, 'Greater than $150,000'],
            [8, 'Skip this question'],
        ],
    )

    numRoommates = models.PositiveIntegerField(
        verbose_name = 'How many people live in the same house or apartment you do, including you?',
        choices = [
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, 'more than 6 total people'],
            [8, 'Skip this question'],
        ],
    )

    maritalStatus = models.PositiveIntegerField(
        verbose_name = 'What is your marital status?',
        choices = [
            [1, 'single'],
            [2, 'married'],
            [3, 'living with partner'],
            [4, 'Skip this question']
        ],
    )

    socialContact = models.PositiveIntegerField(
        verbose_name = 'Not including family members or co-workers, how many friends do you have that you see in person at least once a week?',
        choices = [
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, 'more than 6'],
            [8, 'more than 10'],
            [9, 'Skip this question'],
        ],
    )

    country_born = models.CharField(
        verbose_name = 'In which country were you born?',
        choices = Constants.countries,
    )

    country_reside = models.CharField(
        verbose_name = 'In which country do you currently reside?',
        choices = Constants.countries,
    )
    
    moveYear = models.CharField(
        verbose_name = 'If your current country of residence is different from your country of birth, what year did you come to your country of current residence?',
        choices = [
            'Skip this question',
            '1900',
            '1901',
            '1902',
            '1903',
            '1904',
            '1905',
            '1906',
            '1907',
            '1908',
            '1909',
            '1910',
            '1911',
            '1912',
            '1913',
            '1914',
            '1915',
            '1916',
            '1917',
            '1918',
            '1919',
            '1920',
            '1921',
            '1922',
            '1923',
            '1924',
            '1925',
            '1926',
            '1927',
            '1928',
            '1929',
            '1930',
            '1931',
            '1932',
            '1933',
            '1934',
            '1935',
            '1936',
            '1937',
            '1938',
            '1939',
            '1940',
            '1941',
            '1942',
            '1943',
            '1944',
            '1945',
            '1946',
            '1947',
            '1948',
            '1949',
            '1950',
            '1951',
            '1952',
            '1953',
            '1954',
            '1955',
            '1956',
            '1957',
            '1958',
            '1959',
            '1960',
            '1961',
            '1962',
            '1963',
            '1964',
            '1965',
            '1966',
            '1967',
            '1968',
            '1969',
            '1970',
            '1971',
            '1972',
            '1973',
            '1974',
            '1975',
            '1976',
            '1977',
            '1978',
            '1979',
            '1980',
            '1981',
            '1982',
            '1983',
            '1984',
            '1985',
            '1986',
            '1987',
            '1988',
            '1989',
            '1990',
            '1991',
            '1992',
            '1993',
            '1994',
            '1995',
            '1996',
            '1997',
            '1998',
            '1999',
            '2000',
            '2001',
            '2002',
            '2003',
            '2004',
            '2005',
            '2006',
            '2007',
            '2008',
            '2009',
            '2010',
            '2011',
            '2012',
            '2013',
            '2014',
            '2015',
            '2016',
            '2017',
            '2018',
        ],
    )
    
    city = models.CharField(
        verbose_name = 'What is your city of residence/home?',
        blank = True,
    )
    
    skipCityQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    
    neighborhoodType = models.PositiveIntegerField(
        verbose_name = 'What is the density of your neighborhood',
        choices = [
            [1, 'Rural (mostly farmland)'],
            [2, 'Suburban (large house lots)'],
            [3, 'Urban (small or no lots)'],
            [4, 'Skip this question'],
        ],
    )

    ethnicity = models.PositiveIntegerField(
        verbose_name = 'What is your ethnicity?',
        choices = [
            [1, 'American Indian or Alaska Native'],
            [2, 'Asian'],
            [3, 'Black or African American'],
            [4, 'Hispanic or Latino'],
            [5, 'Native Hawaiian or Other Pacific Islander'],
            [6, 'White or Caucasian'],
            [7, 'Latin American'],
            [8, 'Mixed'],
            [9, 'Unknown'],
            [10, 'Other'],
            [11, 'Skip this question'],
        ],
    )

    degree = models.PositiveIntegerField(
        verbose_name = 'What is your highest degree?',
        choices = [
            [1, 'High School Graduate'],
            [2, 'Some College (no degree)'],
            [3, 'Associate Degree'],
            [4, 'BA/BS'],
            [5, 'JD/MA/MS/MBA/MD'],
            [6, 'PhD/Postdoc'],
            [7, 'Skip this question'],
        ],
    )
    
    major = models.PositiveIntegerField(
        verbose_name = 'What is your professional specialization/major, if applicable?',
        choices = [
            [1, 'Economics'],
            [2, 'Engineering'],
            [3, 'History'],
            [4, 'Mathematics'],
            [5, 'Literature'],
            [6, 'Foreign Language'],
            [7, 'Arts'],
            [8, 'Pyschology'],
            [9, 'Natural Sciences (Biology, Chemistry, Physics)'],
            [10, 'Agriculture'],
            [11, 'Business'],
            [12, 'Education'],
            [13, 'Health Sciences'],
            [14, 'Medicine'],
            [15, 'Law'],
            [16, 'Other liberal arts'],
            [17, 'Other'],
            [18, 'Skip this question'],
        ],
    )

    # 'Have you taken college-level courses in the following subjects?
    subject_econ = models.BooleanField(
        verbose_name = 'Economics',
        widget = widgets.RadioSelectHorizontal()
    )
    
    subject_finance = models.BooleanField(
        verbose_name = 'Finance',
        widget = widgets.RadioSelectHorizontal()
    )
    
    subject_stat = models.BooleanField(
        verbose_name = 'Statistics',
        widget = widgets.RadioSelectHorizontal()
    )
    
    skipSubjectQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end college courses questions
    
    # What is your employment status?  Please check all that apply
    partTime = models.BooleanField(
        verbose_name = 'Part-time paid employment outside the home.',
        widget = widgets.CheckboxInput(),
    )
    
    fullTime = models.BooleanField(
        verbose_name = 'Full-time paid employment outside the home.',
        widget = widgets.CheckboxInput(),
    )
    
    homeEmployed = models.BooleanField(
        verbose_name = 'Part- or full-time paid employment in the home.',
        widget = widgets.CheckboxInput(),
    )
    
    homemaker = models.BooleanField(
        verbose_name = 'Homemaker or other unpaid work in the home.',
        widget = widgets.CheckboxInput(),
    )
    
    fullTimeStudent = models.BooleanField(
        verbose_name = 'Going to school full-time.',
        widget = widgets.CheckboxInput(),
    )
    
    partTimeStudent = models.BooleanField(
        verbose_name = 'Going to school part-time.',
        widget = widgets.CheckboxInput(),
    )
    
    selfEmployed = models.BooleanField(
        verbose_name = 'Self-employed',
        widget = widgets.CheckboxInput(),
    )
    
    lookingWork = models.BooleanField(
        verbose_name = 'Out of work and looking for work',
        widget = widgets.CheckboxInput(),
    )
    
    notLookingWork = models.BooleanField(
        verbose_name = 'Out of work but not currently looking for work',
        widget = widgets.CheckboxInput(),
    )
    
    student = models.BooleanField(
        verbose_name = 'Student',
        widget = widgets.CheckboxInput(),
    )
    
    military = models.BooleanField(
        verbose_name = 'Military',
        widget = widgets.CheckboxInput(),
    )
    
    retired = models.BooleanField(
        verbose_name = 'Retired',
        widget = widgets.CheckboxInput(),
    )
    
    unableWork = models.BooleanField(
        verbose_name = 'Unable to work',
        widget = widgets.CheckboxInput(),
    )
    
    otherWork = models.BooleanField(
        verbose_name = 'Other',
        widget = widgets.CheckboxInput(),
    )
    
    skipWorkQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end employment questions
    
    # 'How do you spend your free time?  Please check all that apply.'
    sports = models.BooleanField(
        verbose_name = 'Play on sports team/club, such as for soccer, football, hockey, basketball, baseball.',
        widget = widgets.CheckboxInput(),
    )
    
    performingArts = models.BooleanField(
        verbose_name = 'Part of a performing arts group such as singing, dancing.',
        widget = widgets.CheckboxInput(),
    )
    
    music = models.BooleanField(
        verbose_name = 'Play a musical instrument in a band or take lessons.',
        widget = widgets.CheckboxInput(),
    )
    
    volunteer = models.BooleanField(
        verbose_name ='Do volunteer work such as work in homeless shelter or package food for the hungry.',
        widget = widgets.CheckboxInput(),
    )
    
    hobby = models.BooleanField(
        verbose_name = 'I have hobbies such as book reading or collecting, drawing, stamp collecting, photography, hiking, bike riding.',
        widget = widgets.CheckboxInput(),
    )
    
    otherFreeTime = models.BooleanField(
        verbose_name = 'Other',
        widget = widgets.CheckboxInput(),
    )    
    
    skipFreeTimeQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end free time questions

    occupation = models.CharField(
        verbose_name = 'What is your occupation, if applicable?',
        blank = True,
    )
    
    skipOccupationQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    
    # How many of the people living in your residence/home are in each of the following age categories?
    residents0to6 = models.PositiveIntegerField(
        verbose_name = 'Less than equal to 6 years?',
        blank = True,
    )
    
    residents7to12 = models.PositiveIntegerField(
        verbose_name = '7 to 12 years?',
        blank = True,
    )
    
    residents13to18 = models.PositiveIntegerField(
        verbose_name = '13 to 18 years?',
        blank = True,
    )
    
    residents19to65 = models.PositiveIntegerField(
        verbose_name = '19 to 65 years?',
        blank = True,
    )
    
    residents65up = models.PositiveIntegerField(
        verbose_name = 'Over 65 years?',
        blank = True,
    )
    
    skipResidentsQ = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end residents age questions
    
    # Of the people 18 years old or younger living in your residence/home, how many participate in each of the following activities?
    activity18School = models.PositiveIntegerField(
        verbose_name = 'Attend day care, school, or college?',
        blank = True,
    )
    
    activity18AfterSchool = models.PositiveIntegerField(
        verbose_name = 'Participate in after-school group activities?',
        blank = True,
    )
    
    activity18Group = models.PositiveIntegerField(
        verbose_name = 'Participate in weekend group activities?',
        blank = True,
    )
    
    activity18Sports = models.PositiveIntegerField(
        verbose_name = 'Play on organized sports team(s)?',
        blank = True,
    )
    
    activity18Flu = models.PositiveIntegerField(
        verbose_name = 'Have taken this year’s flu vaccine?',
        blank = True,
    )
    
    skipActivity18Q = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end activity under 18 questions
    
    # Of the people 19 years old or older living in your residence/home, how many participate in each of the following activities?
    activity19Work = models.PositiveIntegerField(
        verbose_name = 'Work outside the home for wages?',
        blank = True,
    )
    
    activity19School = models.PositiveIntegerField(
        verbose_name = 'Attend school or college?',
        blank = True,
    )
    
    activity19PublicTrans = models.PositiveIntegerField(
        verbose_name = 'Use public transportation?',
        blank = True,
    )
    
    activity19Group = models.PositiveIntegerField(
        verbose_name = 'Participate in evening or weekend group activities?',
        blank = True,
    )
    
    activity19Sports = models.PositiveIntegerField(
        verbose_name = 'Play on organized sports team(s)?',
        blank = True,
    )
    
    activity19Flu = models.PositiveIntegerField(
        verbose_name = 'Have taken this year’s flu vaccine?',
        blank = True,
    )
    
    skipActivity19Q = models.BooleanField(
        verbose_name = 'Skip this question',
        widget = widgets.CheckboxInput(),
    )
    # end activity over 19 questions