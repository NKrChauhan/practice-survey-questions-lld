from survey.survey import Survey
from user.staff_user import StaffUser


class SurveyAnswers:
    def __init__(self, user: StaffUser, survey: Survey, answer_list: list):
        self.user = user
        self.survey = survey
        self.answer_list = answer_list

    def submit(self):
        self.survey.submit_answer_to_survey(user_name=self.user.user_name, answers=self.answer_list)
