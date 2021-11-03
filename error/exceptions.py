class RequiredParamError(Exception):
    def __init__(self, param, field=None):
        self.param = param
        self.field = field
        super().__init__(f'{self.param} is required')

class OptionFormatError(Exception):
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

class EmptyRequestError(Exception):
    def __init__(self, message='Empty JSON request object', field='request JSON body'):
        self.message = message
        self.field = field
        super().__init__(self.message)
