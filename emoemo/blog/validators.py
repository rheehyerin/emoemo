import re
import requests
from django.conf import settings
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
import xmltodict

@deconstructible
class MinLengthValidatior(object):
    def __init__(self, min_length):
        self.min_length = min_length
    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError("{}글자 이상 입력해주세요.".format(self.min_length))