class RasaSapRequest:
    """Class with necessary fields in SAP request.

    Attributes:
        user_name: name of the user.
        action_name: action to take.
        cnn:
        system:
        reference:
    """

    def __init__(self, user_name=None, action_name=None, cnn=None, robot_name=None,
                 system=None, reference=None, creditor=None, buy_org=None, currency=None, pay_cond=None):
        """Inits RasaSapRequest with information"""

        # request params
        self.user_name = user_name
        self.action_name = action_name
        self.robot_name = robot_name
        self.system = system
        self.reference = reference
        self.creditor = creditor
        self.cnn = cnn
        self.buy_org = buy_org
        self.currency = currency
        self.pay_cond = pay_cond
