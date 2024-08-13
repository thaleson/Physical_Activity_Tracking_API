# 📊 API de Monitoramento de Atividades Físicas

Bem-vindo ao projeto de **Monitoramento de Atividades Físicas**! 🏋️‍♂️💪 Esta API permite a gestão de exercícios, metas e treinos para usuários, fornecendo relatórios detalhados e estatísticas sobre o progresso.

## 🚀 Funcionalidades

- **Gerenciamento de Exercícios**: Adicione, edite, visualize e exclua exercícios. 🏃‍♀️
- **Metas e Progresso**: Defina metas e acompanhe seu progresso. 🎯📈
- **Relatórios de Treinos**: Visualize relatórios detalhados sobre seus treinos. 📊

## 📦 Tecnologias Utilizadas

- **Django**: Framework para desenvolvimento web.
- **Django REST Framework**: Framework para criar APIs RESTful.
- **Swagger**: Para documentação interativa da API.
- **drf-yasg**: Para geração de documentação Swagger.

## 🛠️ Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/thaleson/Physical_Activity_Tracking_API
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd seurepositorio
   ```

3. **Crie um ambiente virtual e ative-o:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário para acessar o painel de administração:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```


## 📜 Endpoints

Aqui estão os principais endpoints disponíveis na API:

- **Exercícios**: `/api/exercises/`
- **Metas**: `/api/goals/`
- **Treinos**: `/api/workouts/`
- **Relatório de Progresso das Metas**: `/api/goals/progress/`
- **Estatísticas de Exercícios**: `/api/exercises/statistics/`
- **Relatório de Treinos**: `/api/workouts/report/`

## 🧩 Estrutura do Projeto

- **api/models.py**: Modelos do Django para Exercícios, Metas e Treinos.
- **api/views.py**: Views da API com lógica de negócios e relatórios.
- **api/serializers.py**: Serializadores para transformar dados em JSON.
- **myproject/urls.py**: Configuração das URLs e documentação Swagger.

## 🤝 Contribuindo

Se você quiser contribuir para o projeto, sinta-se à vontade para abrir um **pull request** ou **issue**. Suas contribuições são bem-vindas! 🚀

## 📝 Licença

Este projeto está licenciado sob a **BSD License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.





