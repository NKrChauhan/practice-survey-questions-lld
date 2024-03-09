from user.admin import AdminUser


class Survey:
    def __init__(self, user: AdminUser, questions):
        self.user = user
        self.questions = questions
        self.answers_submitted = {}

    def submit_answer_to_survey(self, user_name, answers):
        if user_name not in self.answers_submitted:
            self.answers_submitted[user_name] = answers
            self.update_avg_for_each_question(answers)

    def update_avg_for_each_question(self, answers):
        answer_index = 0
        for question in self.questions:
            question.update_average(answer=answers[answer_index])
            answer_index += 1
