class RequiredParamError(Exception):
    def __init__(self, param):
        self.param = param
        super().__init__(f'{self.param} is required')

class OptionFormatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmptyRequestError(Exception):
    def __init__(self, message='Empty JSON request object'):
        self.message = message
        super().__init__(self.message)