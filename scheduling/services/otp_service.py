import random
import datetime

from accounts.models import OtpCode
from services import sms_service


class OtpService:
    _message = 'کد احراز هویت شما {}'
    _expire_time = 180  # second

    @classmethod
    def get_otp_object(cls, mobile) -> OtpCode:
        otp = OtpCode.objects.filter(mobile=mobile)
        return otp[0] if len(otp) > 0 else None

    @classmethod
    def delete(cls, obj: OtpCode):
        return obj.delete()

    @classmethod
    def check_code(cls, mobile, code):
        otp = cls.get_otp_object(mobile)
        if otp and otp.code == code and cls.check_deadline(otp):
            return True

    @classmethod
    def check_deadline(cls, obj):
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        interval = now - obj.created_at
        if interval.total_seconds() < cls._expire_time:
            return True

    @classmethod
    def check(cls, mobile):
        obj = cls.get_otp_object(mobile)
        if obj:
            if cls.check_deadline(obj):
                return
            else:
                obj.delete()

        return cls.create(mobile)

    @classmethod
    def create(cls, mobile=None):
        code = random.randint(1000, 9999)
        otp = OtpCode.objects.create(mobile=mobile, code=code)
        cls.show(mobile, code)
        return otp

    @classmethod
    def show(cls, mobile, code):
        return sms_service.send(receptor=mobile, message=cls._message.format(code))
