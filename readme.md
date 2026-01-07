# 🤖 Automação de Testes E2E - Gerenciador de Estoque

Este repositório contém o script de automação desenvolvido em **Python** e **Selenium** para realizar testes de ponta a ponta (End-to-End) no [Gerenciador de Estoque Web](https://estoque-muca.onrender.com).

## 🎯 Objetivo
O script simula a jornada completa de um usuário no sistema, garantindo que as principais funcionalidades (CRUD e Autenticação) estejam operacionais.

## 🚀 Funcionalidades Automatizadas
- **Cadastro Dinâmico:** Gera dados aleatórios para novos usuários.
- **Fluxo de Autenticação:** Login e Logout de conta.
- **Gerenciamento de Inventário:**
  - Cadastro de novos produtos.
  - Busca dinâmica na listagem.
  - Edição de preços e informações.
  - Exclusão de itens com manipulação de alertas JavaScript.

## 🛠️ Diferenciais Técnicos
* **Simulação Humana:** Implementação de digitação cadenciada com intervalos aleatórios para mimetizar o comportamento humano.
* **Resiliência (Wait Strategy):** Configuração de esperas explícitas (`WebDriverWait`) para lidar com o tempo de inicialização do servidor em nuvem (Render).
* **Seletores Avançados:** Uso de **XPath** dinâmico e seletores parciais de link para navegação precisa.

## 📋 Pré-requisitos
* Python 3.x instalado.
* Google Chrome instalado.

## ⚙️ Como executar
1. Instale as dependências necessárias:
   ```bash
   pip install selenium webdriver-manager

2. Execute o script:
    ```bash
python teste_estoqueE2E.py

<p align="center">Projeto desenvolvido para portfólio de estudos em ADS - Unisa</p>