error_codes = {
    'RequiredParamError': 400,
    'EmptyRequestError': 400,
    'OptionFormatError': 422
}

def get_exception_response_and_code(error):
    exception_type = type(error).__name__
    code = error_codes.get(exception_type, 500)
    response = {
        'code': code,
        'reason': str(error)
    }
    return response, code