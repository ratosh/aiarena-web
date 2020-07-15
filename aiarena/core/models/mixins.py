from django_random_queryset import RandomManager
from django.db import DatabaseError

class RandomManagerMixin:
    """Allows selection of a random item from a queryset."""
    objects = RandomManager()


class LockableModelMixin:
    def lock_me(self, nowait=False) -> bool:
        # todo: is there a better way to do this?
        try:
            self.__class__.objects.select_for_update(nowait=nowait).get(id=self.id)
            self.refresh_from_db()
            return True
        except DatabaseError:
            print("Could not lock")
            return False
