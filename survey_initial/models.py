from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = "Brian J. Goode & Ethan Vu"

doc = """
Sociodemographics Survey.
"""


class Constants(BaseConstants):
    name_in_url = "survey_initial"
    players_per_group = None
    num_rounds = 1
    countries = [
        "AD - Andorra",
        "AE - United Arab Emirates",
        "AF - Afghanistan",
        "AG - Antigua and Barbuda",
        "AI - Anguilla",
        "AL - Albania",
        "AM - Armenia",
        "AO - Angola",
        "AQ - Antarctica",
        "AR - Argentina",
        "AS - American Samoa",
        "AT - Austria",
        "AU - Australia",
        "AW - Aruba",
        "AZ - Azerbaijan",
        "BA - Bosnia and Herzegovina",
        "BB - Barbados",
        "BD - Bangladesh",
        "BE - Belgium",
        "BF - Burkina Faso",
        "BG - Bulgaria",
        "BH - Bahrain",
        "BI - Burundi",
        "BJ - Benin",
        "BL - Saint Barthelemy",
        "BM - Bermuda",
        "BN - Brunei",
        "BO - Bolivia",
        "BR - Brazil",
        "BS - Bahamas, The",
        "BT - Bhutan",
        "BV - Bouvet Island",
        "BW - Botswana",
        "BY - Belarus",
        "BZ - Belize",
        "CA - Canada",
        "CC - Cocos (Keeling) Islands",
        "CD - Congo, Democratic Republic of the",
        "CF - Central African Republic",
        "CG - Congo, Republic of the",
        "CH - Switzerland",
        "CI - Cote d\"Ivoire",
        "CK - Cook Islands",
        "CL - Chile",
        "CM - Cameroon",
        "CN - China",
        "CO - Colombia",
        "CR - Costa Rica",
        "CU - Cuba",
        "CV - Cape Verde",
        "CW - Curacao",
        "CX - Christmas Island",
        "CY - Cyprus",
        "CZ - Czech Republic",
        "DE - Germany",
        "DJ - Djibouti",
        "DK - Denmark",
        "DM - Dominica",
        "DO - Dominican Republic",
        "DZ - Algeria",
        "EC - Ecuador",
        "EE - Estonia",
        "EG - Egypt",
        "EH - Western Sahara",
        "ER - Eritrea",
        "ES - Spain",
        "ET - Ethiopia",
        "FI - Finland",
        "FJ - Fiji",
        "FK - Falkland Islands (Islas Malvinas)",
        "FM - Micronesia, Federated States of",
        "FO - Faroe Islands",
        "FR - France",
        "FX - France, Metropolitan",
        "GA - Gabon",
        "GD - Grenada",
        "GE - Georgia",
        "GF - French Guiana",
        "GG - Guernsey",
        "GH - Ghana",
        "GI - Gibraltar",
        "GL - Greenland",
        "GM - Gambia, The",
        "GN - Guinea",
        "GP - Guadeloupe",
        "GQ - Equatorial Guinea",
        "GR - Greece",
        "GS - South Georgia and the Islands",
        "GT - Guatemala",
        "GU - Guam",
        "GW - Guinea-Bissau",
        "GY - Guyana",
        "HK - Hong Kong",
        "HM - Heard Island and McDonald Islands",
        "HN - Honduras",
        "HR - Croatia",
        "HT - Haiti",
        "HU - Hungary",
        "ID - Indonesia",
        "IE - Ireland",
        "IL - Israel",
        "IM - Isle of Man",
        "IN - India",
        "IO - British Indian Ocean Territory",
        "IQ - Iraq",
        "IR - Iran",
        "IS - Iceland",
        "IT - Italy",
        "JE - Jersey",
        "JM - Jamaica",
        "JO - Jordan",
        "JP - Japan",
        "KE - Kenya",
        "KG - Kyrgyzstan",
        "KH - Cambodia",
        "KI - Kiribati",
        "KM - Comoros",
        "KN - Saint Kitts and Nevis",
        "KP - Korea, North",
        "KR - Korea, South",
        "KW - Kuwait",
        "KY - Cayman Islands",
        "KZ - Kazakhstan",
        "LA - Laos",
        "LB - Lebanon",
        "LC - Saint Lucia",
        "LI - Liechtenstein",
        "LK - Sri Lanka",
        "LR - Liberia",
        "LS - Lesotho",
        "LT - Lithuania",
        "LU - Luxembourg",
        "LV - Latvia",
        "LY - Libya",
        "MA - Morocco",
        "MC - Monaco",
        "MD - Moldova",
        "ME - Montenegro",
        "MF - Saint Martin",
        "MG - Madagascar",
        "MH - Marshall Islands",
        "MK - Macedonia",
        "ML - Mali",
        "MM - Burma",
        "MN - Mongolia",
        "MO - Macau",
        "MP - Northern Mariana Islands",
        "MQ - Martinique",
        "MR - Mauritania",
        "MS - Montserrat",
        "MT - Malta",
        "MU - Mauritius",
        "MV - Maldives",
        "MW - Malawi",
        "MX - Mexico",
        "MY - Malaysia",
        "MZ - Mozambique",
        "NA - Namibia",
        "NC - New Caledonia",
        "NE - Niger",
        "NF - Norfolk Island",
        "NG - Nigeria",
        "NI - Nicaragua",
        "NL - Netherlands",
        "NO - Norway",
        "NP - Nepal",
        "NR - Nauru",
        "NU - Niue",
        "NZ - New Zealand",
        "OM - Oman",
        "PA - Panama",
        "PE - Peru",
        "PF - French Polynesia",
        "PG - Papua New Guinea",
        "PH - Philippines",
        "PK - Pakistan",
        "PL - Poland",
        "PM - Saint Pierre and Miquelon",
        "PN - Pitcairn Islands",
        "PR - Puerto Rico",
        "PS - Gaza Strip",
        "PS - West Bank",
        "PT - Portugal",
        "PW - Palau",
        "PY - Paraguay",
        "QA - Qatar",
        "RE - Reunion",
        "RO - Romania",
        "RS - Serbia",
        "RU - Russia",
        "RW - Rwanda",
        "SA - Saudi Arabia",
        "SB - Solomon Islands",
        "SC - Seychelles",
        "SD - Sudan",
        "SE - Sweden",
        "SG - Singapore",
        "SH - Saint Helena, Ascension, and Tristan da Cunha",
        "SI - Slovenia",
        "SJ - Svalbard",
        "SK - Slovakia",
        "SL - Sierra Leone",
        "SM - San Marino",
        "SN - Senegal",
        "SO - Somalia",
        "SR - Suriname",
        "SS - South Sudan",
        "ST - Sao Tome and Principe",
        "SV - El Salvador",
        "SX - Sint Maarten",
        "SY - Syria",
        "SZ - Swaziland",
        "TC - Turks and Caicos Islands",
        "TD - Chad",
        "TF - French Southern and Antarctic Lands",
        "TG - Togo",
        "TH - Thailand",
        "TJ - Tajikistan",
        "TK - Tokelau",
        "TL - Timor-Leste",
        "TM - Turkmenistan",
        "TN - Tunisia",
        "TO - Tonga",
        "TR - Turkey",
        "TT - Trinidad and Tobago",
        "TV - Tuvalu",
        "TW - Taiwan",
        "TZ - Tanzania",
        "UA - Ukraine",
        "UG - Uganda",
        "UM - United States Minor Outlying Islands",
        "UK - United Kingdom",
        "US - United States",
        "UY - Uruguay",
        "UZ - Uzbekistan",
        "VA - Holy See (Vatican City)",
        "VC - Saint Vincent and the Grenadines",
        "VE - Venezuela",
        "VG - British Virgin Islands",
        "VI - Virgin Islands",
        "VN - Vietnam",
        "VU - Vanuatu",
        "WF - Wallis and Futuna",
        "WS - Samoa",
        "XK - Kosovo",
        "YE - Yemen",
        "YT - Mayotte",
        "ZA - South Africa",
        "ZM - Zambia",
        "ZW - Zimbabwe",
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    lastName = models.StringField(
        verbose_name = "Last Name",
    )
    
    firstName = models.StringField(
        verbose_name = "First Name",
    )
    
    middleInitial = models.StringField(
        verbose_name = "Middle Initial",
        max_length = 1,
    )
    
    age = models.PositiveIntegerField(
        verbose_name = "What is your age (years)?",
    )

    sexBirth = models.StringField(
        verbose_name = "ASSIGNED SEX AT BIRTH: What sex were you assigned at birth (on your original birth certificate)?",
        choices = [
            "Male",
            "Female",
        ],
        widget = widgets.RadioSelect,
    )
    
    sexCurrent = models.StringField(
        verbose_name = "CURRENT GENDER IDENTITY:  How do you describe yourself? (check one)?",
        choices = [
            "Male",
            "Female",
            "Transgender",
            "Do not identify as female, male, or transgender",
        ],
        widget = widgets.RadioSelect,
    )

    ethnicity = models.StringField(
        verbose_name = "Enter your ethnic group, if you identify with one.",
    )
    
    # TODO: Modify "Please specify" options s.t. if choice selected, must fill out please specify
    race = models.PositiveIntegerField(
        verbose_name = "What is your race?",
        choices = [
            [1, "White"],
            [2, "Black or African American"],
            [3, "American Indian or Alaska Native"],
            [4, "Asian Indian"],
            [5, "Japanese"],
            [6, "Native Hawaiian"],
            [7, "Chinese"],
            [8, "Korean"],
            [9, "Guaminian or Chamorro"],
            [10, "Filipino"],
            [11, "Vietnamese"],
            [12, "Samoan"],
            [13, "Other Asian"],
            [14, "Other Pacific Islander"],
            [15, "Some other race"],
        ],
        widget = widgets.RadioSelect,
    )
    
    tribe = models.StringField(
        verbose_name = "(print names of enrolled or principle tribe)",
        blank = True,
    )
    
    otherAsian = models.StringField(
        verbose_name = "(print race)",
        blank = True,
    )
    
    otherPacificIslander = models.StringField(
        verbose_name = "(print race)",
        blank = True,
    )
    
    otherRace = models.StringField(
        verbose_name = "(print race)",
        blank = True,
    )
    
    maritalStatus = models.PositiveIntegerField(
        verbose_name = "What is your marital status?",
        choices = [
            [1, "Single"],
            [2, "Married"],
            [3, "Divorced"],
            [4, "Separated"],
            [5, "Widowed"],
        ],
        widget = widgets.RadioSelect,
    )
    
    country_born = models.StringField(
        verbose_name = "In which country were you born?",
        choices = Constants.countries,
    )

    # What is your current residence?
    country_reside = models.StringField(
        verbose_name = "Country",
        choices = Constants.countries,
    )
    
    province_reside = models.StringField(
        verbose_name = "State/Province",
        blank = True,
    )
    
    city_reside = models.StringField(
        verbose_name = "City",
    )
    # end residence questions
    
    reside_len = models.PositiveIntegerField(
        verbose_name = "How long have you been at your current residence?",
    )
    
    socialContact = models.PositiveIntegerField(
        verbose_name = "Not including family members or co-workers, how many of your friends do you see weekly? ",
    )
    
    degree = models.PositiveIntegerField(
        verbose_name = "What is your highest degree?",
        choices = [
            [1, "High School Graduate"],
            [2, "Some College (no degree)"],
            [3, "Associate Degree"],
            [4, "BA/BS"],
            [5, "JD/MA/MS/MBA/MD"],
            [6, "PhD/Postdoc"],
            [7, "Skip this question"],
        ],
        widget = widgets.RadioSelect,
    )
    
    major = models.PositiveIntegerField(
        verbose_name = "If you are a college graduate what was your major?",
        choices = [
            [1, "Economics"],
            [2, "Engineering"],
            [3, "History"],
            [4, "Mathematics"],
            [5, "Literature"],
            [6, "Foreign Language"],
            [7, "Arts"],
            [8, "Psychology"],
            [9, "Natural Sciences (Biology, Chemistry, Physics)"],
            [10, "Agriculture"],
            [11, "Business"],
            [12, "Education"],
            [13, "Health Sciences"],
            [14, "Medicine"],
            [15, "Law"],
            [16, "Other liberal arts"],
            [17, "Other"],
        ],
        widget = widgets.RadioSelect,
    )
    
    # "Have you taken college-level courses in the following subjects?
    subject_econ = models.BooleanField(
        verbose_name = "Economics",
        widget = widgets.RadioSelectHorizontal()
    )
    
    subject_finance = models.BooleanField(
        verbose_name = "Finance",
        widget = widgets.RadioSelectHorizontal()
    )
    
    subject_stat = models.BooleanField(
        verbose_name = "Statistics",
        widget = widgets.RadioSelectHorizontal()
    )
    # end college courses questions
    
    # What is your employment status? Please check all that apply.
    partTime = models.BooleanField(
        verbose_name = "Part-time paid employment outside the home",
        widget = widgets.CheckboxInput(),
    )
    
    fullTime = models.BooleanField(
        verbose_name = "Full-time paid employment outside the home",
        widget = widgets.CheckboxInput(),
    )
    
    homeEmployed = models.BooleanField(
        verbose_name = "Part- or full-time paid employment in the home",
        widget = widgets.CheckboxInput(),
    )
    
    homemaker = models.BooleanField(
        verbose_name = "Homemaker or other unpaid work in the home",
        widget = widgets.CheckboxInput(),
    )
    
    fullTimeStudent = models.BooleanField(
        verbose_name = "Going to school full-time",
        widget = widgets.CheckboxInput(),
    )
    
    partTimeStudent = models.BooleanField(
        verbose_name = "Going to school part-time",
        widget = widgets.CheckboxInput(),
    )
    
    selfEmployed = models.BooleanField(
        verbose_name = "Self-employed",
        widget = widgets.CheckboxInput(),
    )
    
    lookingWork = models.BooleanField(
        verbose_name = "Out of work and looking for work",
        widget = widgets.CheckboxInput(),
    )
    
    notLookingWork = models.BooleanField(
        verbose_name = "Out of work but not currently looking for work",
        widget = widgets.CheckboxInput(),
    )
    
    military = models.BooleanField(
        verbose_name = "Military",
        widget = widgets.CheckboxInput(),
    )
    
    retired = models.BooleanField(
        verbose_name = "Retired",
        widget = widgets.CheckboxInput(),
    )
    
    unableWork = models.BooleanField(
        verbose_name = "Unable to work",
        widget = widgets.CheckboxInput(),
    )
    
    otherWork = models.BooleanField(
        verbose_name = "Other",
        widget = widgets.CheckboxInput(),
    )
    
    otherWorkSpecify = models.StringField(
        verbose_name = "(print other)",
        blank = True,
    )
    # end employment questions
    
    # How do you spend your free time?  Please check all that apply.
    sports = models.BooleanField(
        verbose_name = "Play on sports team/club, such as for soccer, football, hockey, basketball, baseball",
        widget = widgets.CheckboxInput(),
    )
    
    performingArts = models.BooleanField(
        verbose_name = "Part of a performing arts group such as singing, dancing",
        widget = widgets.CheckboxInput(),
    )
    
    music = models.BooleanField(
        verbose_name = "Play a musical instrument in a band or take lessons",
        widget = widgets.CheckboxInput(),
    )
    
    volunteer = models.BooleanField(
        verbose_name ="Do volunteer work such as work in homeless shelter or package food for the hungry",
        widget = widgets.CheckboxInput(),
    )
    
    hobby = models.BooleanField(
        verbose_name = "I have hobbies such as book reading or collecting, drawing, stamp collecting, photography, hiking, bike riding, etc.",
        widget = widgets.CheckboxInput(),
    )
    
    otherFreeTime = models.BooleanField(
        verbose_name = "Other",
        widget = widgets.CheckboxInput(),
    )
    
    otherFreeTimeSpecify = models.StringField(
        verbose_name = "(print other)",
        blank = True,
    )
    # end free time questions
    
    occupation = models.StringField(
        verbose_name = "What is your occupation, if applicable?",
    )
    
    # Household Information
    income = models.PositiveIntegerField(
        verbose_name = "What is your annual household income, in U.S. dollars?",
        choices = [
            [1, "Less than $25,000"],
            [2, "$25,000 - $49,999"],
            [3, "$50,000 - $89,999"],
            [4, "$90,000 - $149,999"],
            [5, "Greater than $150,000"],
        ],
        widget = widgets.RadioSelect,
    )

    numRoommates = models.PositiveIntegerField(
        verbose_name = "How many people live in your residence?",
    )
    
    # How many of the people living in your residence are in each of the following age categories?
    residents0to6 = models.PositiveIntegerField(
        verbose_name = "Less than equal to 6 years?",
    )
    
    residents7to12 = models.PositiveIntegerField(
        verbose_name = "7 to 12 years?",
    )
    
    residents13to18 = models.PositiveIntegerField(
        verbose_name = "13 to 18 years?",
    )
    
    residents19to65 = models.PositiveIntegerField(
        verbose_name = "19 to 65 years?",
    )
    
    residents65up = models.PositiveIntegerField(
        verbose_name = "Over 65 years?",
    )
    # end residents age questions
    
    # Of the people living in your residence, how many ...
    activitySchool = models.PositiveIntegerField(
        verbose_name = "Attend day care, school, or college?",
    )
    
    activityAfterSchool = models.PositiveIntegerField(
        verbose_name = "Participate in after-school group activities?",
    )
    
    activityGroup = models.PositiveIntegerField(
        verbose_name = "Participate in weekend group activities?",
    )
    
    activitySports = models.PositiveIntegerField(
        verbose_name = "Play on organized sports team(s)?",
    )
    
    activityFlu = models.PositiveIntegerField(
        verbose_name = "Have taken this year’s flu vaccine?",
    )
    
    activityWork = models.PositiveIntegerField(
        verbose_name = "Work outside the home for wages?",
    )
    
    activityPubTrans = models.PositiveIntegerField(
        verbose_name = "Use public transportation?",
    )
    
    activityEvening = models.PositiveIntegerField(
        verbose_name = "Participate in evening or weekend group activities?",
    )
    
    activityCollegeClubs = models.PositiveIntegerField(
        verbose_name = "Participate in college clubs and organizations?"
    )
    
    activityPartTimeWork = models.PositiveIntegerField(
        verbose_name = "Have a part-time job?"
    )
    # end activity questions
    
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
    
    selflessness = models.PositiveIntegerField(
        verbose_name = "How do you see yourself? In comparison to others are you a person who is generally willing to give up something today in order to benefit from that in the future, or are you not willing to do so in comparison to others? Please indicate your answer on a scale from 0 to 10, where a 0 means \"not at all willing to give up something\", and a 10 means \"very willing to give up something\". You can use the values in between to indicate where you fall on the scale.",
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
    
    trustingness = models.PositiveIntegerField(
        verbose_name = "How well does the following statement describe you as a person? As long as I am not convinced otherwise, I assume that people have only the best intentions. Please indicate your answer on a scale from 0 to 10. A 0 means \"does not describe me at all\", a 10 means \"describes me very well\". You can use the values in between to indicate where you fall on the scale.",
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
    
    donation = models.PositiveIntegerField(
        verbose_name = "Imagine the following situation: you won 1,000 Euro in a lottery. Considering your current situation, how much would you donate to charity?",
        max = 1000,
    )
    
    punishInclination = models.PositiveIntegerField(
        verbose_name = "How do you see yourself? Are you a person who is generally willing to punish unfair behavior even if it is costly? Please indicate your answer on a scale from 0 to 10. A 0 means “not at all willing to punish”, a 10 means “very willing to punish”. You can use the values in between to indicate where you fall on the scale.",
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
    # end preference elicitation
    
    # start preference module i
    timeScenerio_1 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "100$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_2 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "103$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_3 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "106.10$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_4 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "109.20$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_5 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "112.40$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_6 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "115.60$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_7 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "118.80$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_8 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "122.10$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_9 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "125.40$"],
        ],
        widget = widgets.RadioSelectHorizontal,
    )
    
    timeScenerio_10 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "128.80$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_11 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "132.30$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_12 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "135.70$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_13 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "139.20$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_14 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "142.80$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_15 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "146.40$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_16 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "150.10$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_17 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "153.80$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_18 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "157.50$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_19 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "161.30$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_20 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "165.10$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_21 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "169.00$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_22 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "172.90$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_23 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "176.90$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_24 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "180.90$"],
        ],
        widget = widgets.RadioSelect,
    )
    
    timeScenerio_25 = models.PositiveIntegerField(
        choices = [
            [1, "100$"],
            [2, "185.00$"],
        ],
        widget = widgets.RadioSelect,
    )
    # end preference module i
    
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