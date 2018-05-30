from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()
try:
    validate('sad')
except ValidationError as e:
    print(e)