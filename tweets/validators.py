from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Content can not be blank")
    return value
