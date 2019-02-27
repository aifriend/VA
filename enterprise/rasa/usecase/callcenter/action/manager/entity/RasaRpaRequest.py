class RasaRpaRequest:
    """Class with necessary fields in RASA RPA request.

    Attributes:
        user_name: name of the intent.
        robot_name: entities in the question.
        creditor:
        cnn:
        buy_org:
        currency:
        pay_cond:

    """

    def __init__(self, user_name=None, robot_name=None, creditor=None, cnn=None, buy_org=None, currency=None, pay_cond=None):
        """Inits RasaRpaRequest with information"""

        self.user_name = user_name
        self.robot_name = robot_name
        self.creditor = creditor
        self.cnn = cnn
        self.buy_org = buy_org
        self.currency = currency
        self.pay_cond = pay_cond
