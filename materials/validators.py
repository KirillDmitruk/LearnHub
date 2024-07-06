from rest_framework.serializers import ValidationError


class YouTubeValidation:
    """ Валидатор для поля ссылки на YouTube """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)  # OrderedDict переводим в dict, и получаем зн. поля, которое нужно валидировать.
        if "youtube.com" not in val:
            raise ValidationError("Ссылка на видео должна быть только на youtube.com!")
