import json


def json_response(car, response):
    if car is None:
        return {"errorCode": 404, "message": response}
    return json.dumps(car.to_dict())


def json_bool_response(result):
    if result:
        return {"errorCode": 200, "message": "Success"}
    return {"errorCode": 404, "message": "Entity not found"}


def jdefault(o):
    """
    Define how deserialize an entity
    :param o:
    :return: entity dictonnary
    """
    if isinstance(o, set):
        return list(o)
    return o.__dict__


def error_handler(code, message, response):
    """
    Return an error  code and the associated message
    :param code:
    :param message:
    :param response:
    :return:
    """
    response.status = code
    return json.dumps({
        'code': code,
        'message': message
    })


def get_record_from_body(request, record_type):
    """
    Build an entity object with json
    :param request:
    :param record_type:
    :return: entity object
    """
    body = request.body
    body_str = body.read().decode('utf-8')
    return record_type(**json.loads(body_str))