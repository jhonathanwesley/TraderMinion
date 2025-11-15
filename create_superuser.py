from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@localhost', 'admin123')
    print("Superusuário 'admin' criado com sucesso!")
else:
    print("Superusuário 'admin' já existe!")
