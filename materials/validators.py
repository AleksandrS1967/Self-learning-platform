from rest_framework.serializers import ValidationError


class Validate:

    def __init__(self, user, obj):
        self.user = user
        self.obj = obj

    def validate_lesson(self):
        object_group_set = self.user.groups.filter(name="moderator")
        check_bool = False
        if len(object_group_set) == 0:
            check_bool = False
        else:
            object_group = self.user.groups.get(name="moderator")
            if object_group:
                check_bool = str(object_group) == "moderator"
        if self.user == self.obj.course.owner or check_bool:
            pass
        else:
            raise ValidationError(
                "Вы должны быть владельцем курса к которому "
                "создаете данный урок. - или модератором! "
                f"Вы - {self.user}. "
                f"Владелец курса - {self.obj.course.owner}"
            )

    def validate_test(self):
        object_group_set = self.user.groups.filter(name="moderator")
        check_bool = False
        if len(object_group_set) == 0:
            check_bool = False
        else:
            object_group = self.user.groups.get(name="moderator")
            if object_group:
                check_bool = str(object_group) == "moderator"
        if self.user == self.obj.lesson.owner or check_bool:
            pass
        else:
            raise ValidationError(
                "Вы должны быть владельцем урока к которому "
                "создаете данный тест. - или модератором! "
                f"Вы - {self.user}. "
                f"Владелец урока - {self.obj.lesson.owner}"
            )
