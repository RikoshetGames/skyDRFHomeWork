from rest_framework.exceptions import ValidationError

ALLOWED_DOMAINS = (
    'youtube.com',
)


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get(self.field)
        if not url:
            return

        for allowed_domain in ALLOWED_DOMAINS:
            if allowed_domain in url:
                return

        raise ValidationError('Ссылки на сторонние видео запрещены')