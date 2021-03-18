from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import child_c_crf_3000

child_pool_schedule_1 = Schedule(
    name='child_pool_schedule1',
    verbose_name='Pool Schedule V1',
    onschedule_model='flourish_child.onschedulechildpool',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit3000 = Visit(
    code='3000',
    title='Child Pool Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_3000,
    facility_name='5-day clinic')

schedule_helper = ScheduleHelper(visit=visit3000, crfs=child_c_crf_3000,
                                 schedule=child_pool_schedule_1, visit4000=None)
schedule_helper.create_quarterly_visits()

child_pool_schedule_1.add_visit(visit=visit3000)
