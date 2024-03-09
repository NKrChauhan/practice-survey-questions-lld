from survey.option.option import Option
from survey.question.question import SurveyQuestion
from survey.survey import Survey
from survey_answers.survey_answers import SurveyAnswers
from user.admin import AdminUser
from user.staff_user import StaffUser

if __name__ == '__main__':
    admin_user = AdminUser("admin_user")
    questions = []
    survey_question_1 = SurveyQuestion(admin_user, "What is UI/UX like?")
    option_list = [
        Option(survey_question_1, "1", 1),
        Option(survey_question_1, "2", 2),
        Option(survey_question_1, "3", 3),
        Option(survey_question_1, "4", 4),
    ]
    survey_question_1.set_option_list(option_list)
    questions.append(survey_question_1)
    survey_question_2 = SurveyQuestion(admin_user, "What is like?")
    option_list_2 = [
        Option(survey_question_2, "1", 1),
        Option(survey_question_2, "2", 2),
        Option(survey_question_2, "3", 3),
        Option(survey_question_2, "4", 4),
    ]
    survey_question_2.set_option_list(option_list_2)
    questions.append(survey_question_2)
    survey_form = Survey(user=admin_user)
    survey_form.create_survey(questions)

    for index in range(4):
        staff_user = StaffUser(f"my_answer_{index}")
        answer = SurveyAnswers(user=staff_user, survey=survey_form, answer_list=["1", "4"])
        answer.submit()
    print(survey_question_1.get_avg_score())
    print(survey_question_1.number_of_submissions)
    print(survey_question_2.get_avg_score())
    print(survey_question_2.number_of_submissions)
