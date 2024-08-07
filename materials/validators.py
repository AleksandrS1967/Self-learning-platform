from rest_framework.serializers import ValidationError
from materials.models import Course


class Validate:

    def __init__(self, user, obj):
        self.user = user
        self.obj = obj

    def validate_lesson(self):
        if self.user != self.obj.course.owner or self.user.groups.filter(name="moderator"):
            raise ValidationError('Вы должны быть владельцем курса к которому '
                                  'создаете данный урок. - или модератором! '
                                  f'Вы - {self.user}. '
                                  f'Владелец курса - {self.obj.course.owner}')