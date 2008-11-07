import os
import train

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    requires_model_validation = False
    can_import_settings = False
        
    def handle(self, *args, **options):
        
        # get filesystem directory for skeleton
        template_dir = os.path.join(train.__path__[0], 'skeleton')

        # get filesystem directory for current project
        current_dir = os.getcwd()

        # copy directory structure into current directory
        for d, subdirs, files in os.walk(template_dir):
            relative_dir = d[len(template_dir)+1:]
            if relative_dir:
                try:
                    os.mkdir(os.path.join(current_dir, relative_dir))
                except OSError:
                    pass
            for i, subdir in enumerate(subdirs):
                if subdir.startswith('.'):
                    del subdirs[i]
            for f in files:
                if f.endswith('.pyc'):
                    continue
                path_old = os.path.join(d, f)
                path_new = os.path.join(current_dir, relative_dir, f)
                fp_old = open(path_old, 'r')
                # we only want to write to files that don't exist
                try:
                    file_exists = open(path_new, 'r')
                except IOError:
                    fp_new = open(path_new, 'w')
                    fp_new.write(fp_old.read())
                    fp_new.close()
                fp_old.close()