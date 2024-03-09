from survey.survey import Survey
from user.base import BaseUser


class SurveyAnswers:
    def __init__(self, user: BaseUser, survey: Survey, answer_list: list):
        self.user = user
        self.survey = survey
        self.answer_list = answer_list

    def submit(self):
        if not self.user.has_permission_to_submit_survey():
            raise Exception("User is not permitted for this action")
        self.survey.submit_answer_to_survey(user=self.user, answers=self.answer_list)
