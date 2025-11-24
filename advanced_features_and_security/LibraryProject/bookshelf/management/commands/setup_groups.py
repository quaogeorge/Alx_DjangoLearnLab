from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Create default groups (Editors, Viewers, Admins) and assign bookshelf permissions'

    def handle(self, *args, **options):
        # Get permission objects for Book's custom permissions
        app_label = 'bookshelf'
        perm_codenames = ['can_view', 'can_create', 'can_edit', 'can_delete']

        permissions = []
        for codename in perm_codenames:
            try:
                perm = Permission.objects.get(content_type__app_label=app_label, codename=codename)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Permission {app_label}.{codename} not found. Have you run makemigrations & migrate?'))
                return
            permissions.append(perm)

        # Create / update groups
        viewers, created = Group.objects.get_or_create(name='Viewers')
        editors, created = Group.objects.get_or_create(name='Editors')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Assign permissions:
        viewers.permissions.set([p for p in permissions if p.codename == 'can_view'])
        editors.permissions.set([p for p in permissions if p.codename in ('can_view', 'can_create', 'can_edit')])
        admins.permissions.set(permissions)  # full set

        viewers.save()
        editors.save()
        admins.save()

        self.stdout.write(self.style.SUCCESS('Groups (Viewers, Editors, Admins) created/updated with permissions.'))