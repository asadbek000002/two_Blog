import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Actions


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Actions.objects.filter(user__id=user.id,
                                             verb=verb,
                                             create__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
                                            target_ct=target_ct,
                                            target_id=target.id)
    if not similar_actions:
        action = Actions(user=user, verb=verb, target=target)
        action.save()
        return True
    return False