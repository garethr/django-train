from django.core.management.base import BaseCommand

class Command(BaseCommand):
        
    def handle(self, *args, **options):
        print "Hello world"
        # get filesystem directory for skeleton
        # get filesystem directory for current project
        # copy contents of skeleton into current project