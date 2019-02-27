class RepoComponentsFactory:

    @staticmethod
    def get_auth_service():
        from watson_assistant.auth_service.AuthService import AuthService
        return AuthService()

    @staticmethod
    def get_wd_service():
        from watson_assistant.wd_service.WdService import WdService
        return WdService()
