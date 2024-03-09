from user.base import BaseUser


class SurveyQuestion:
    def __init__(self, user: BaseUser, question_name: str):
        self.user = user
        self.question_name = question_name
        self.avg_score = 0
        self.number_of_submissions = 0
        self.option_list = None

    def set_option_list(self, option_list):
        self.option_list = option_list

    def update_average(self, answer):
        new_submission_score = self.number_of_submissions+1
        score_for_current_answer = self.get_score_for_answer(answer)
        self.avg_score = (self.number_of_submissions * self.avg_score + score_for_current_answer) / new_submission_score
        self.number_of_submissions += 1

    def get_score_for_answer(self, answer):
        for option in self.option_list:
            if option.option_name == answer:
                return option.score
        return 0

    def get_avg_score(self):
        if self.user.has_permission_to_check_evaluation():
            return self.avg_score
        raise Exception("Permission not granted to see avg score")
