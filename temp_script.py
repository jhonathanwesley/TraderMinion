from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@localhost', 'admin123') if not User.objects.filter(username='admin').exists() else None
