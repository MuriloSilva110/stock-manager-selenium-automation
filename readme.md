🤖 Automação de Testes E2E - Gerenciador de Estoque
<div align="center"> <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Selenium-4.0+-43B02A?logo=selenium&logoColor=white" alt="Selenium"> <img src="https://img.shields.io/badge/WebDriver_Manager-Automated-00ADEE?logo=selenium&logoColor=white" alt="WebDriver Manager"> <img src="https://img.shields.io/badge/Unisa-ADS-005596" alt="Unisa"> </div>

Garantia de Qualidade e Confiabilidade: Script de automação desenvolvido para validar o ciclo completo de vida (E2E) do Gerenciador de Estoque Web. Focado em testes de regressão e estabilidade de sistemas em nuvem.

🎯 Objetivo Técnico
O script simula a jornada real de um usuário final, garantindo que as regras de negócio e a persistência de dados no PostgreSQL (Backend) permaneçam operacionais após novas implementações.

🚀 Cobertura de Testes
Autenticação: Validação de login, registro dinâmico de usuários e logout.

Integridade do CRUD: Cadastro, edição, filtragem e exclusão de produtos com validação de banco de dados.

Navegação UI: Interação com alertas JavaScript e elementos dinâmicos do Bootstrap 5.

🛠️ Soluções de Engenharia
Resiliência (Wait Strategy): Implementação de WebDriverWait com esperas explícitas de até 120s para sincronizar com a inicialização do servidor no Render.

Human-Like Interaction: Função personalizada para emular a velocidade de digitação humana, reduzindo a taxa de bloqueios e aumentando a fidelidade do teste.

Seletores Dinâmicos: Uso estratégico de XPath e seletores CSS para navegação em tabelas de dados dinâmicas.

📋 Pré-requisitos
Python 3.x

Google Chrome (Browser estável)

WebDriver Manager (Incluso no script para gerenciamento automático do driver)

⚙️ Instalação e Execução
Instale as dependências:
```bash
pip install selenium webdriver-manager
```
Execute a suíte de testes:
```bash
python teste_estoqueE2E.py
```
<p align="center">Murilo Silva - Estudante de ADS na Unisa | Aspirante a Engenheiro de Dados e Backend 🚀</p>
