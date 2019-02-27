class ComponentsFactory:
    """Handles requests to Factory Components
    """

    def __init__(self):
        pass

    @staticmethod
    def get_business_logic_dialog_manager():
        """Handles requests to Business Logic Service
        """
        from service.manager.BusinessLogicDialogManager import BusinessLogicDialogManager
        return BusinessLogicDialogManager()

    @staticmethod
    def get_natural_language_understander():
        """Handles requests to NLU Service
        """
        from service.manager.NluDialogManager import NluDialogManager
        return NluDialogManager()

    @staticmethod
    def get_repository_dialog_manager():
        """Handles requests to Repository Service
        """
        from service.manager.RepositoryDialogManager import RepositoryDialogManager
        return RepositoryDialogManager()

    @staticmethod
    def get_rasa_dialog_manager():
        """Handles requests to Rasa Service
        """
        from service.manager.RasaDialogManager import RasaDialogManager
        return RasaDialogManager()

    @staticmethod
    def get_security_dialog_manager():
        """Handles requests to Security Service
        """
        from service.manager.SecurityDialogManager import SecurityDialogManager
        return SecurityDialogManager()

    @staticmethod
    def get_context_dialog_manager():
        """Handles requests to Context Service
        """
        from service.manager.ContextDialogManager import ContextDialogManager
        return ContextDialogManager()

    @staticmethod
    def get_confidence_manager():
        """Handles requests to Confidence Controller Service
        """
        from service.manager.ConfidenceDialogManager import ConfidenceDialogManager
        return ConfidenceDialogManager()
