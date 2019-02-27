class IAuthorizationService:

    def __init__(self):
        pass

    def check_authorization(self, email):
        """
        Check user authorization
        :param email:
        :return:
        """
        raise NotImplementedError()
