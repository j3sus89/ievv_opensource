from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'Set the passwords of all users to "test". Very useful ' \
           'when loading a production dump locally for testing/debugging.'

    def handle_noargs(self, **options):
        user_model = get_user_model()
        user_model.objects.all().update(password=make_password('test'))
