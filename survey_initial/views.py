from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    template_name = "survey_initial/intro.html"
    
class SocioDemographic(Page):
    form_model = models.Player
    is_debug = False

    def makeCheckTable(self, qName, choices, table_rows):
                      
        header = ''.join(['<th class="verticalTableHeader"><div><p>{}</p></div></th>'.format(c) for c in choices])
        row = """
            <tr>
                <td><div class="row-text">{}</div></td>
                {}
            </tr>
            """
            
        def make_data_row(field,i):
            cells = []
            for c in choices:
                i += 1
                title = 'q14_{}_{}X{}'.format(i,field[0],c)
                field_name = "id_{}".format(title)
                name = field
                data_row = """
                    <td><div class="btnRadio">
                        <label class="checkbox no-margin" for="{}">
                            <input type="checkbox" id="{}" value=True name="{}"> 
                        </label>
                    </div></td>
                """.format(field_name, field_name, title)
                cells.append(data_row)
            
            return ''.join(cells), i           
        
        rows = []
        i = 0
        for table_row in table_rows:
            data, i = make_data_row(table_row, i)             
            rows.append(row.format(table_row[1],data))
                
        rows = '\n'.join(rows)
            
            
        out_str = """<table class="table table-condensed fixed" summary="" >
          <colgroup>
    <col style="background-color:white; width: 400px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
  </colgroup>
    <thead>
        <tr>
            <th></th>
            {}
        </tr>    
    </thead>
    <tbody>
        {}
    </tbody>
    </table>"""
        return out_str.format(header,rows)

    def makeTable(self, qName = 'q12'):
        fields = [fname for fname in self.form_model._meta.get_all_field_names() if fname.startswith(qName)]
        fields = sorted(fields)
        rows = []
        choices = self.form_model._meta.get_field_by_name(fields[0])[0].choices
                      
        header = ''.join(['<th class="verticalTableHeader"><div><p>{}</p></div></th>'.format(c[0]) for c in choices])

        def make_data_row(field):
            cells = []
            i = 0
            for c in choices:
                field_name = "id_{}_{}".format(field,i+1)
                name = field
                i += 1
                data_row = """
                <td><div class="btnRadio">
                <label class="radio-inline" for="{}">
                <input type="radio" id="{}" value="{}" name="{}" required> 
                </label>
                </div></td>""".format(field_name, field_name, c[0], name)
                cells.append(data_row)
            
            return ''.join(cells)           
        row = """
        <tr>
            <td><div class="row-text">{}</div></td>
            {}
        </tr>
        """ 
        for field in fields:
            F = self.form_model._meta.get_field_by_name(field)
            f = F[0]
            
            if f.choices:
                rows.append(row.format(f.verbose_name,make_data_row(field)))
                
        rows = '\n'.join(rows)
            
            
        out_str = """<table class="table table-condensed fixed" summary="" >
          <colgroup>
    <col style="background-color:white; width: 400px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
    <col style="background-color:#eee; width: 30px;">
    <col style="background-color:#fff; width: 30px;">
  </colgroup>
    <thead>
        <tr>
            <th></th>
            {}
        </tr>    
    </thead>
    <tbody>
        {}
    </tbody>
    </table>"""
        return out_str.format(header,rows)   
    
    def get_form_fields(self):
        questions = [
            "q1_birthYear",
            
            "q2a_placeOfBirth_country",
            "q2b_placeOfBirth_state",
            "q2c_placeOfBirth_city",
            
            "q3a_permanentHome_country",
            "q3b_permanentHome_state",
            "q3c_permanentHome_city",
            
            "q4_ethnicity",
            
            "q5a_race_Asian",
            "a5b_race_Black",
            "q5c_race_AmericanIndian",
            "q5d_race_NativeHawaiian",
            "q5e_race_White",
            "q5f_race_Other",
            "q5g_race_OtherPrint",
            
            "q6a_sexGender",
            "q6b_sexGender_other",
            
            "q7_maritalStatus",
            
            "q8a_education_overview",
            "q8b_education_other",
            "q8c_education_freshman",
            "q8d_education_sophomore",
            "q8e_education_junior",
            "q8f_education_senior",
            "q8g_education_masters",
            "q8h_education_phD",
            "q8i_education_eds",
            "q8j_education_edd",
            
            "q9_major",
            "q9_majorOther",
            
            "q10a_subject_econ",
            "q10b_subject_finance",
            "q10c_subject_stat",
            
            "q11_military_service",
            
            "q12a_activities_academic",
            "q12b_activities_exercise",
            "q12c_activities_sports",
            "q12d_activities_performing",
            "q12e_activites_religious",
            "q12f_activites_membership",
            "q12g_activities_leading",
            "q12h_activities_socializing",
            "q12i_activities_socialNetworks",
            "q12j_activities_onlineGames",
            "q12k_activities_partying",
            "q12l_activities_working",
            "q12m_activities_household",
            "q12n_activities_other",
            "q12o_activities_otherPrint",
            
            "q13a_transportation",
            "q13b_volunteer",
            "q13c_donations",
            "q13d_discussPolitics",
            "q13e_communicate",
            "q13f_demonstrate",
            "q13g_elections",
            "q13h_risk",

            "q14_l_networking_otherPrint",            
            
            "q15a_ethics_wealth",
            "q15b_ethics_climate",
            "q15c_ethics_gunControl",
            "q15d_ethics_admissions",
            "q15e_ethics_taxes",
            
        ]

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
        ]
        
        rows = [
            ("prof_network", "Professional networking"),
            ("soc_network", "Social networking"),
            ("xchng_info", "Exchange of information with peers and family"),
            ("soc_events","Organize and/or attend social events"),
            ("pol_events","Organize and/or attend political events"),
            ("news_info", "News and Information about people and places"),
            ("job", "Job seeking"),
            ("money", "To make money"),
            ("games", "To play games"),
            ("research", "Research"),
            ("other", "Other"),
            ("dont_use","I don’t use this social networking site"),
        ]
        i = 0
        for r in rows:
            for c in columns:
                i += 1
                field_name = 'q14_{}_{}X{}'.format(i, r[0], c)
                questions += [field_name]        
        
        return questions

    def vars_for_template(self):

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
        ]
        
        rows = [
            ("prof_network", "Professional networking"),
            ("soc_network", "Social networking"),
            ("xchng_info", "Exchange of information with peers and family"),
            ("soc_events","Organize and/or attend social events"),
            ("pol_events","Organize and/or attend political events"),
            ("news_info", "News and Information about people and places"),
            ("job", "Job seeking"),
            ("money", "To make money"),
            ("games", "To play games"),
            ("research", "Research"),
            ("other", "Other"),
            ("dont_use","I don’t use this social networking site"),
        ]        
        
        return {
            'q12Table':  self.makeTable('q12').replace('\n',''),
            'q13Table':  self.makeTable('q13').replace('\n',''),
            'q14Table':  self.makeCheckTable('q14', columns, rows),
            'q15Table':  self.makeTable('q15').replace('\n',''),       
        }


class Behavioral1(Page):
    form_model = models.Player
    form_fields = [
        "daringness",
        "risky_project",
        "risky_project_2",
    ] + ['coinScenerio_{}'.format(i) for i in range(1, 32)]
    
    def vars_for_template(self):
        return {'coinOffers': [{"num": i, "amt": 10 * (i - 1)} for i in range(1, 32)]}


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


class Behavioral3(Page):
    form_model = models.Player
    form_fields = ['coinScenerio_{}'.format(i) for i in range(1, 32)]
    
    def vars_for_template(self):
        return {'coinOffers': [{"num": i, "amt": 10 * (i - 1)} for i in range(1, 32)]}

    
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
#    Intro,
    SocioDemographic,
    Behavioral1,
    Results,
]
