# myproject/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à API de Monitoramento de Atividades Físicas. Acesse /swagger/ para a documentação.")
