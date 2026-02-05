# Start-SE

## Descrição do Projeto

O Start-SE é uma plataforma web desenvolvida em Django que visa **conectar empresários em busca de captação de investimentos com investidores interessados em novas oportunidades**. A aplicação facilita o processo de investimento, permitindo que empresários apresentem seus projetos de forma profissional e investidores encontrem e apoiem empresas promissoras.

## Objetivos

*   **Principal:** Conectar investidores com empresários.
*   **Gerais:**
    *   Permitir o cadastro de usuários (empresários e investidores) com nome e senha.
    *   Oferecer funcionalidades distintas para cada tipo de usuário após o login.

## Funcionalidades

### Para Empresários

*   **Cadastro e Gerenciamento de Empresas:** Permite que empresários cadastrem informações detalhadas sobre suas empresas, incluindo tempo de existência, estágio de desenvolvimento, área de atuação, público-alvo, valor de captação desejado e percentual de equity oferecido.
*   **Upload de Mídias:** Possibilidade de fazer upload de pitchs (apresentações) e logotipos da empresa.
*   **Documentação e Métricas:** Adição e gerenciamento de documentos relevantes e métricas de desempenho para cada empresa.
*   **Status de Captação:** Visualização clara do status de captação (em andamento ou finalizada) e cálculo automático do valuation da empresa.
*   **Gerenciamento de Propostas:** Visualizar investidores interessados, incluindo o valor que cada um deseja investir, e decidir se aceita ou recusa as propostas de investimento.
*   **Acompanhamento Financeiro:** Acompanhar informações como o valor total estimado da empresa, o total disponível para captação e o total já captado.

### Para Investidores

*   **Exploração de Empresas:** Navegação e visualização de empresas cadastradas na plataforma, com acesso aos detalhes do projeto, pitchs e documentos na seção "Marketplace".
*   **Propostas de Investimento:** Funcionalidade para realizar propostas de investimento, especificando valor e percentual de participação.
*   **Gerenciamento de Propostas:** Acompanhamento do status das propostas (aguardando assinatura, enviada, aceita, recusada).
*   **Verificação de Identidade:** Upload de selfie e RG para fins de verificação e segurança nas transações.

### Funcionalidades Gerais

*   **Autenticação de Usuários:** Sistema de cadastro e login para empresários e investidores.
*   **Painel Administrativo:** Interface de administração Django para gerenciamento de usuários e dados da plataforma.

## Tecnologias Utilizadas

*   **Backend:** Python, Django
*   **Banco de Dados:** SQLite (padrão, configurável para outros SGBDs)
*   **Frontend:** HTML, CSS (com arquivos estáticos organizados por app)

## Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o Python 3.x e o `pip` instalados em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/Luiz-ROCampos/Start-SE.git
cd Start-SE
```

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate    # No Windows
```

### 3. Instalar Dependências

Como não há um arquivo `requirements.txt` explícito no repositório, as dependências básicas do Django serão instaladas. Você pode precisar instalar outras bibliotecas conforme o uso.

```bash
pip install Django
```

### 4. Configurar o Banco de Dados

Execute as migrações para criar as tabelas no banco de dados.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um Superusuário (Opcional)

Para acessar o painel administrativo do Django, crie um superusuário.

```bash
python manage.py createsuperuser
```

### 6. Rodar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

O projeto estará acessível em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

O projeto é organizado nos seguintes aplicativos Django:

*   `core/`: Contém as configurações globais do projeto, URLs principais e arquivos de configuração WSGI/ASGI.
*   `usuarios/`: Responsável pelo gerenciamento de usuários, incluindo cadastro e autenticação (login/logout).
*   `empresarios/`: Lida com as funcionalidades específicas para empresários, como cadastro e gerenciamento de empresas, documentos e métricas. Inclui modelos como `Empresas`, `Documento` e `Metricas`.
*   `investidores/`: Implementa as funcionalidades para investidores, como a visualização de empresas, realização e gerenciamento de propostas de investimento (`PropostaInvestimento`).

## Contribuição

Se você deseja contribuir com este projeto, por favor, siga as boas práticas de desenvolvimento e abra um Pull Request com suas alterações.

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT). Veja o arquivo `LICENSE` para mais detalhes. (Assumindo licença MIT, caso não haja um arquivo LICENSE explícito no repositório).

## Autor

Luiz-ROCampos

---
