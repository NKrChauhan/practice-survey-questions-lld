from survey.question.question import SurveyQuestion


class Option:
    def __init__(self, question: SurveyQuestion, option_name, score):
        self.question = question
        self.option_name = option_name
        self.score = score
