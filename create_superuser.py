#!/usr/bin/env python
"""
Script para criar superusuário padrão
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@localhost', 'admin123')
    print("Superusuário 'admin' criado com sucesso!")
    print("Usuário: admin")
    print("Senha: admin123")
else:
    print("Superusuário 'admin' já existe!")
