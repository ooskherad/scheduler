from kavenegar import *
from scheduling import settings


def send(receptor, message):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'sender': '',
            'receptor': receptor,
            'message': message,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
