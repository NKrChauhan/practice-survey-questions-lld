from user.base import BaseUser


class Survey:
    def __init__(self, user: BaseUser):
        self.user = user
        self.questions = None
        self.answers_submitted = {}

    def create_survey(self, questions):
        if self.user.has_permission_to_publish_question_paper():
            self.questions = questions
        else:
            raise Exception("Permission not granted to create a survey")

    def submit_answer_to_survey(self, user, answers):
        if user.has_permission_to_submit_survey() and user.user_name not in self.answers_submitted:
            self.answers_submitted[user.user_name] = answers
            self.update_avg_for_each_question(answers)

    def update_avg_for_each_question(self, answers):
        answer_index = 0
        for question in self.questions:
            question.update_average(answer=answers[answer_index])
            answer_index += 1

    def get_all_submitted_answers(self):
        if self.user.has_permission_to_check_evaluation():
            return self.answers_submitted
        raise Exception("Permission not granted to see answers of survey")
