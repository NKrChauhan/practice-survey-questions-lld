from user.base import BaseUser
from user.constants import UserType


class StaffUser(BaseUser):
    user_type = UserType.STAFF

    def has_permission_to_publish_question_paper(self):
        return False

    def has_permission_to_check_evaluation(self):
        return False

    def has_permission_to_submit_survey(self):
        return True
