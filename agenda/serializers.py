import datetime
from rest_framework import serializers
from agenda.models import Agendamento
from django.utils import timezone 
"""Um serializer é uma classe que converte dados complexos, como instanceetos Python, em tipos de dados que podem ser 
facilmente renderizados em JSON, XML, ou outros formatos, e vice-versa"""

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'data_horario', 'nome_cliente', 'email_cliente', 'telefone_cliente']
    
    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Agendamento não pode ser feito no passado")
        return value
    
    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")

        if email_cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("E-mail brasileiro deve estar associado a um número do Brasil (+55)")
        return attrs

   