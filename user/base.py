from abc import abstractmethod


class BaseUser:
    user_type = None

    def __init__(self, name):
        self.user_name = name

    def get_user_type(self):
        return self.user_type

    def get_user_name(self):
        return self.user_name

    @abstractmethod
    def has_permission_to_publish_question_paper(self):
        raise NotImplemented

    @abstractmethod
    def has_permission_to_check_evaluation(self):
        raise NotImplemented

    @abstractmethod
    def has_permission_to_submit_survey(self):
        raise NotImplemented
