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
    years = list(range(2018,1900))
    countries = [
        "US - United States",
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
    # Question 1
    q1_birthYear = models.IntegerField(
        verbose_name = "1. Birth year",
        choices = list(range(2018,1900,-1)),
    )

    # Question 2
    q2a_placeOfBirth_country = models.CharField(
        verbose_name = "Country",
        choices = Constants.countries,    
    )
    
    q2b_placeOfBirth_state = models.CharField(
        verbose_name = "State/Province, if applicable",
        blank = True,
    )
    
    q2c_placeOfBirth_city = models.CharField(
        verbose_name = "City",    
    )
    
#    # Question 3
#    q3a_permanentHome_country = models.CharField(
#        verbose_name = "Country",
#        choices = Constants.countries,    
#    )
#    
#    q3b_permanentHome_state = models.CharField(
#        verbose_name = "State/Province, if applicable",
#        blank = True,
#    )
#    
#    q3c_permanentHome_city = models.CharField(
#        verbose_name = "City",    
#    )

    # Question 4
    q4_ethnicity = models.CharField(
        verbose_name = "Ethinic Groups (one or more)",
        blank = True,
    )

    # Question 5
    q5a_race_Asian = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,
        )
    a5b_race_Black = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,
    )
    q5c_race_AmericanIndian = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q5d_race_NativeHawaiian = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q5e_race_White = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q5f_race_Other = models.BooleanField(
        blank = True,
        widget = widgets.CheckboxInput,
    )
    q5g_race_OtherPrint = models.CharField(
        verbose_name = "If other, please specify:",
        blank = True,
    )
    q5h_race_noAnswer = models.CharField(
        widget = widgets.CheckboxInput,
        blank = True,
    )

    # Question 6
    q6a_sexGender = models.CharField(
        verbose_name = "Sex/Gender",
        choices = [
            "Male",
            "Female",
            "Transgender",
            "Other",
            "Prefer not to answer",
        ],
        widget = widgets.RadioSelect,
    )
    
    q6b_sexGender_other = models.CharField(
        verbose_name = "If other, please print",
        blank = True,    
    )
    
    # Question 7
    q7_maritalStatus = models.CharField(
        verbose_name = "Marital status",
        choices = [
            "Single, never married",
            "Married",
            "Divorced",
            "Separated",
            "Widowed",
        ],
        widget = widgets.RadioSelect,
    )    

    # Question 8    
    q8a_education_overview = models.CharField(
        verbose_name = "Education status",
        choices = [
            'Undergraduate Student',
            'Graduate Student',
            'Post-graduate Student',
            'Faculty',
            'High School or Equivalent',
            'Other',
        ],
        widget = widgets.RadioSelect,    
    )
    q8b_education_other = models.CharField(
        verbose_name = "If other, please specify",
        blank = True,    
    )
    q8c_education_freshman = models.BooleanField(
        verbose_name = "Freshman",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8d_education_sophomore = models.BooleanField(
        verbose_name = "Sophomore",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8e_education_junior = models.BooleanField(
        verbose_name = "Junior",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8f_education_senior = models.BooleanField(
        verbose_name = "Senior",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8g_education_masters = models.BooleanField(
        verbose_name = "Masters",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8h_education_phD = models.BooleanField(
        verbose_name = "PhD",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8i_education_eds = models.BooleanField(
        verbose_name = "Ed.S",
        blank = True,
        widget = widgets.CheckboxInput,    
    )
    q8j_education_edd = models.BooleanField(
        verbose_name = "Ed.D",
        blank = True,
        widget = widgets.CheckboxInput,    
    )

    
    # Question 9
    q9_major = models.CharField(
        verbose_name = "What is your major?",
        choices = sorted([
            "Arts (Performing or Visual)",
            "History",
            "Business",
            "Languages and literature",
            "Philosophy",
            "Theology",
            "Anthropology",
            "Economics",
            "Finance",
            "Education"
            "Agriculture",
            "Geography",
            "Law",
            "Political science",
            "Psychology",
            "Sociology",
            "Biology",
            "Chemistry",
            "Earth sciences",
            "Space sciences",
            "Physics",
            "Computer Science",
            "Mathematics",
            "Statistics",
            "Engineering and technology",
            "Medicine and health",            
            ]) + ["Other"],
    )
    q9_majorOther = models.CharField(
        verbose_name = "If other, please specify",
        blank = True,
        )

    # Question 10
    q10a_subject_econ = models.BooleanField(
        verbose_name = "Economics",
        widget = widgets.RadioSelectHorizontal()
    )
    
    q10b_subject_finance = models.BooleanField(
        verbose_name = "Finance",
        widget = widgets.RadioSelectHorizontal()
    )
    
    q10c_subject_stat = models.BooleanField(
        verbose_name = "Statistics",
        widget = widgets.RadioSelectHorizontal()
    )    
    
    # Question 11
    q11_military_service = models.BooleanField(
        verbose_name = "Do you currently serve or have you ever served in the military? (e.g., ROTC, cadet, or midshipman at a service academy; In the Reserves or National Guard; A discharged veteran)",
        widget = widgets.RadioSelectHorizontal()
    )    
    
    # Question 12
    q12a_activities_academic = models.CharField(
        verbose_name = "Academic / school activities (classes, homework, studying)",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',        
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12b_activities_exercise = models.CharField(
        verbose_name = "Exercise or individual sports",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',        
        ],
        widget = widgets.RadioSelectHorizontal(),   
    )
    q12c_activities_sports = models.CharField(
        verbose_name = "Playing on a sports team/club, such as for soccer, football, hockey, basketball, baseball",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',    
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12d_activities_performing = models.CharField(
        verbose_name = "Performing in an arts group such as choir, dance troop, band, orchestra",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',   
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q12e_activites_religious = models.CharField(
        verbose_name = "Attending religious services/activities",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',       
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q12f_activites_membership = models.CharField(
        verbose_name = "Membership activities (e.g., student clubs/groups)",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',       
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12g_activities_leading = models.CharField(
        verbose_name = "Leading groups/clubs/organizations",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',        
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12h_activities_socializing = models.CharField(
        verbose_name = "Socializing with friends in person",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',       
        ],
        widget = widgets.RadioSelectHorizontal(),
    )
    q12i_activities_socialNetworks = models.CharField(
        verbose_name = "Online social networks (Facebook, Twitter, etc.)",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',     
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12j_activities_onlineGames = models.CharField(
        verbose_name = "Online games",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',       
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
    q12l_activities_working = models.CharField(
        verbose_name = "Working (for pay)",
        choices = [
            'None',
            'Less than 1 hour',
            '1-5 hours',
            '6-10 hours',
            '11-20 hours',
            'Over 20 hours',     
        ],
        widget = widgets.RadioSelectHorizontal(),    
    )
#    q12n_activities_other = models.CharField(
#        verbose_name = "Other",
#        choices = [
#            'None',
#            'Less than 1 hour',
#            '1-5 hours',
#            '6-10 hours',
#            '11-20 hours',
#            'Over 20 hours',       
#        ],
#        widget = widgets.RadioSelectHorizontal(),
#        blank = True,    
#    )
#    q12o_activities_otherPrint = models.CharField(
#        verbose_name = "If other, please print",
#        blank = True, 
#    ) 
    
        
        
