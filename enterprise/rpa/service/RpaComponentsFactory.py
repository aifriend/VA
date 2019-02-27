class RpaComponentsFactory:

    @staticmethod
    def get_aros_service():
        from rpa_service.aros_service.ArosService import ArosService
        return ArosService()

    @staticmethod
    def get_sqs_service():
        from rpa_service.sqs_service.SqsService import SqsService
        return SqsService()
