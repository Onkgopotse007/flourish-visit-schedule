from edc_visit_schedule import Crf, FormsCollection

crfs_prn = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.cliniciannotes',
        required=False, additional=False),
    Crf(show_order=2, model='flourish_caregiver.caregiversocialworkreferral',
        required=False, additional=False),
    name='caregiver_crf_prn')

crfs_prn_referral = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.caregiversocialworkreferral',
        required=False, additional=False),
    name='caregiver_ref_crf_prn')

crf_pre_consent = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    name='pre_flourish')

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.cliniciannotes'),
    name='unscheduled')

post_referral_unscheduled = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.caregiverphqpostreferral',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.caregivergadpostreferral',
        required=False),
    Crf(show_order=3, model='flourish_caregiver.caregiveredinburghpostreferral',
        required=False),
    name='pr_unscheduled')

crfs_tb6month = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.tbinterviewtranscription'),
    Crf(show_order=2, model='flourish_caregiver.tbinterviewtranslation'),
    name='tb_6month')

a_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.hivrapidtestcounseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.ultrasound',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.tbstudyeligibility', required=False),
    Crf(show_order=6, model='flourish_caregiver.maternalhivinterimhx',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=8, model='flourish_caregiver.arvsprepregnancy',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.maternalarvduringpreg',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.substanceusepriorpregnancy',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregiverclinicalmeasurements',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=13, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.caregiverphqreferralfu',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.caregiveredinburghreferral',
        required=False),
    Crf(show_order=17, model='flourish_caregiver.caregiveredinburghreferralfu',
        required=False),
    Crf(show_order=18, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=19, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=20, model='flourish_caregiver.caregivergadreferralfu',
        required=False),
    Crf(show_order=21, model='flourish_caregiver.tbhistorypreg',
        required=False),
    Crf(show_order=22, model='flourish_caregiver.tbroutinehealthscreen', required=False),
    Crf(show_order=23, model='flourish_caregiver.tbroutinehealthscreenv2'),
    Crf(show_order=24, model='flourish_caregiver.obstericalhistory',
        required=False),
    Crf(show_order=25, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=26, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=27, model='flourish_caregiver.relationshipfatherinvolvement'),
    Crf(show_order=28, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=29, model='flourish_caregiver.maternalarvadherence', required=False),
    Crf(show_order=30, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=31, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),
    Crf(show_order=32, model='flourish_caregiver.caregiversafistigma'),

    name='cohort_a_enrollment')

bc_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.hivrapidtestcounseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.obstericalhistory',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.caregiverclinicalmeasurements',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=8, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.caregiverphqreferralfu',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=11, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregivergadreferralfu',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=17, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=18, model='flourish_caregiver.relationshipfatherinvolvement'),
    Crf(show_order=19, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=20, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=21, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),
    Crf(show_order=22, model='flourish_caregiver.maternalarvadherence', required=False),
    Crf(show_order=23, model='flourish_caregiver.caregiversafistigma'),

    name='cohort_bc_enrollment')

crf_2000d = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.hivrapidtestcounseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.maternalarvatdelivery',
        required=False),
    Crf(show_order=3, model='flourish_caregiver.caregiverclinicalmeasurements',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.substanceuseduringpregnancy'),
    Crf(show_order=5, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=6, model='flourish_caregiver.maternalinterimidcc',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.maternalinterimidccversion2'),
    Crf(show_order=8, model='flourish_caregiver.tbroutinehealthscreen', required=False),
    Crf(show_order=9, model='flourish_caregiver.tbroutinehealthscreenv2'),
    Crf(show_order=10, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=11, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=12, model='flourish_caregiver.tbstudyeligibility', required=False),
    Crf(show_order=13, model='flourish_caregiver.maternalarvpostadherence'),
    Crf(show_order=14, model='flourish_caregiver.caregiverphqpostreferral',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.caregivergadpostreferral',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.caregiveredinburghpostreferral',
        required=False),
    name='birth')

crf_2001 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.posthivrapidtestandconseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=4, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=8, model='flourish_caregiver.maternalinterimidcc',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.maternalinterimidccversion2'),
    Crf(show_order=10, model='flourish_caregiver.tbstudyeligibility', required=False),
    Crf(show_order=11, model='flourish_caregiver.breastfeedingquestionnaire',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.relationshipfatherinvolvement',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.caregiverphqpostreferral',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.caregivergadpostreferral',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.caregiveredinburghpostreferral',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.maternalarvpostadherence'),
    Crf(show_order=17, model='flourish_caregiver.interviewfocusgroupinterest',
        required=False),
    Crf(show_order=18, model='flourish_caregiver.interviewfocusgroupinterestv2',
        required=False),
    Crf(show_order=19, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=20, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=21, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),
    name='quarterly_calls')

a_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.posthivrapidtestandconseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=6, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=7, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=8, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.caregiverphqreferralfu',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregivergadreferralfu',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.caregiveredinburghreferral',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.caregiveredinburghreferralfu',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=16, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=17, model='flourish_caregiver.maternalinterimidcc',
        required=False),
    Crf(show_order=18, model='flourish_caregiver.maternalinterimidccversion2', ),
    Crf(show_order=19, model='flourish_caregiver.relationshipfatherinvolvement'),
    Crf(show_order=20, model='flourish_caregiver.maternalarvpostadherence'),

    Crf(show_order=21, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=22, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=23, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),

    Crf(show_order=24, model='flourish_caregiver.caregiversafistigma'),

    name='a_follow_up')

b_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.posthivrapidtestandconseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=5, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=8, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=9, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=10, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregiverphqreferralfu',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.caregivergadreferralfu',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.caregiveredinburghreferral',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.caregiveredinburghreferralfu',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=17, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=18, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=19, model='flourish_caregiver.relationshipfatherinvolvement'),
    Crf(show_order=20, model='flourish_caregiver.maternalarvpostadherence'),
    Crf(show_order=21, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=22, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=23, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=24, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),
    Crf(show_order=25, model='flourish_caregiver.caregiversafistigma'),

    name='b_follow_up')

c_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.posthivrapidtestandconseling',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=3, model='flourish_caregiver.medicalhistory',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=5, model='flourish_caregiver.hivdisclosurestatusa',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.hivdisclosurestatusb',
        required=False),
    Crf(show_order=7, model='flourish_caregiver.hivdisclosurestatusc',
        required=False),
    Crf(show_order=8, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=9, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=10, model='flourish_caregiver.caregiverphqreferral',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregiverphqreferralfu',
        required=False),
    Crf(show_order=12, model='flourish_caregiver.caregivergadreferral',
        required=False),
    Crf(show_order=13, model='flourish_caregiver.caregivergadreferralfu',
        required=False),
    Crf(show_order=14, model='flourish_caregiver.caregiveredinburghreferral',
        required=False),
    Crf(show_order=15, model='flourish_caregiver.caregiveredinburghreferralfu',
        required=False),
    Crf(show_order=16, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=17, model='flourish_caregiver.covid19', required=False),
    Crf(show_order=18, model='flourish_caregiver.relationshipfatherinvolvement'),
    Crf(show_order=19, model='flourish_caregiver.maternalarvpostadherence'),
    Crf(show_order=20, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=21, model='flourish_caregiver.caregivertbscreening'),
    Crf(show_order=22, model='flourish_caregiver.tbreferralcaregiver'),
    Crf(show_order=23, model='flourish_caregiver.caregivertbreferraloutcome',
        required=False),
    Crf(show_order=24, model='flourish_caregiver.caregiversafistigma'),

    name='c_follow_up')

tb_2_months = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.tbvisitscreeningwomen'),
    Crf(show_order=2, model='flourish_caregiver.tbroutinehealthscreen', required=False),
    Crf(show_order=3, model='flourish_caregiver.tbroutinehealthscreenv2'),
    Crf(show_order=4, model='flourish_caregiver.tbpresencehouseholdmembers'),
    Crf(show_order=5, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=6, model='flourish_caregiver.cliniciannotes'),
    Crf(show_order=7, model='flourish_caregiver.tbreferral', required=False),
    name='tb_2_months')

tb_6_months = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.tbengagement'),
    Crf(show_order=2, model='flourish_caregiver.tbknowledge'),
    Crf(show_order=3, model='flourish_caregiver.tbreferraloutcomes'),
    Crf(show_order=4, model='flourish_caregiver.tbinterview', required=False),
    Crf(show_order=5, model='flourish_caregiver.tbinterviewtranscription',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.tbinterviewtranslation', required=False),
    Crf(show_order=7, model='flourish_caregiver.cliniciannotes'),
    name='tb_6_months')
