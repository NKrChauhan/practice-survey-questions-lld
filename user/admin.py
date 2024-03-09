from user.base import BaseUser
from user.constants import UserType


class AdminUser(BaseUser):
    user_type = UserType.ADMIN

    def has_permission_to_publish_question_paper(self):
        return True

    def has_permission_to_check_evaluation(self):
        return True

    def has_permission_to_submit_survey(self):
        return False
