import time   # Para dar pausas fixas (dormir)
import random # Para sortear números (pausas aleatórias)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select , WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- FUNÇÃO AUXILIAR ---
# Esta função recebe um elemento (campo) e o texto.
# Ela digita letra por letra, esperando um tempo aleatório entre elas.
def digitar_humano(elemento, texto):
    for letra in texto:
        elemento.send_keys(letra)
        # Sorteia um tempo entre 0.1s e 0.3s
        time.sleep(random.uniform(0.1, 0.3))



if __name__ == "__main__":
    # Configura o driver do Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    #options.add_experimental_option("detach", True)  # Mantém o navegador aberto após o script terminarS
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver , 120)

    try:

        #-----------Gera um usuario para teste automatizado----------------
        cod = random.randint(1000, 9999)
        usuariao_fake = f'Usuario{cod}'
        email_fake = f'Tester{cod}@test.com'
        senha_fake = 123456
        #------------------------------------------------------------------    

        # Abre o site do Google
        driver.get("https://estoque-muca.onrender.com")
        
        #TESTE CADASTRO DE USUARIO 
        #Encontra e esperar a pagina principal carregar e o botao de cadsatro aparecer e clica assim que ele aparece visivel na tela
        link_cadastro = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Cadastrar"))).click()
        
        #-------Preenche o formulario de cadastro-------------------------------------- 
        campo_nome = driver.find_element(By.NAME, "username")
        digitar_humano(campo_nome, usuariao_fake)

        campo_email = driver.find_element(By.NAME, "email")
        digitar_humano(campo_email, email_fake)
      
        campo_senha = driver.find_element(By.NAME, "senha")
        digitar_humano(campo_senha, senha_fake)
    
        campo_confirmacao = driver.find_element(By.NAME, "confirm_senha")
        digitar_humano(campo_confirmacao, senha_fake)
  
        # Submete o formulário
        campo_confirmacao.send_keys(Keys.ENTER)
        #--------------------------------------------------------------------------------
        # O site redireciona automaticamente para pagina de login apos cadastro
        #--------------------------------------------------------------------------------
        # Teste pagina de login
        #-------preenche formulario de login---------------------------------------------
        campo_email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        digitar_humano(campo_email, email_fake)
        time.sleep(1)
        
        campo_senha = driver.find_element(By.NAME, "senha")
        digitar_humano(campo_senha, senha_fake)
        time.sleep(1)
        # Preenche o ccampo senha e envia o formulario
        campo_senha.send_keys(Keys.ENTER)
        #------------------------------------------------------------------------------
        # TESTE ADICIONAR NOVO PRODUTO 
        #-------Acessa formulario novo pruduto---------------------------------------------------------------------------
        link_adicinar_prod = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Adicionar Produto"))).click()
        time.sleep(1)
        #-------Preenche os campos de novo produto-----------------------------------------------------------------------
        campo_nome_produto = driver.find_element(By.NAME, "nome")
        digitar_humano(campo_nome_produto,"Cadeira Gamer RGB" )
        time.sleep(1)
        campo_preco = driver.find_element(By.NAME, "preco")
        digitar_humano(campo_preco, "1200.00")
        time.sleep(1)
        campo_codigo_interno = driver.find_element(By.NAME, "codigo_interno")
        digitar_humano(campo_codigo_interno, f'GM-{cod}')
        time.sleep(1)
        # Encontra o dropdow de selecao de fornecedor 
        elemento_fornecedor = driver.find_element(By.NAME, "fornecedor_id")
        # seleciona um elemento na lista dropdown  
        select_fornecedor = Select(elemento_fornecedor)
        select_fornecedor.select_by_index(0)
        time.sleep(1)
        # Encontra o dropdow de selecao de fornecedor 
        elemento_categoria = driver.find_element(By.NAME, "categoria_id")
        select_categoria = Select(elemento_categoria)
        select_categoria.select_by_index(0)
        time.sleep(1)

        campo_submit = driver.find_element(By.NAME, "submit").click()

        # encontra barra de busca 
        campo_busca = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
        digitar_humano(campo_busca, 'Dell')
        campo_busca.send_keys(Keys.RETURN)

        # Encotra e clica no botao editar do primeiro elemento da lista de busca  
        link_editar = driver.find_element(By.PARTIAL_LINK_TEXT, 'Editar').click()
        time.sleep(2)

        #Apaga e preenche e edita os dados no formularrio 
        campo_novo_preco = driver.find_element(By.ID, "preco")
        campo_novo_preco.clear()
        
        digitar_humano(campo_novo_preco, "950.0")
        time.sleep(2)

        #Clica no butao para atualizar o produto
        campo_submit_novo_pd = driver.find_element(By.ID, "submit").click()


        # Encotra e clica em excluir para excluir um produto 
       
        nome_produto = "CAD-Ergo"
        xpath_magico = f"//td[contains(text(), '{nome_produto}')]/parent::tr//a[contains(text(), 'Excluir')]"

        driver.find_element(By.XPATH, xpath_magico).click()
        time.sleep(2)

        # Muda o foco do robô para a janelinha de alerta
        alerta = driver.switch_to.alert
        alerta.accept() # Clica no "OK"

        # Volta para a Home 
        link_home = driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(2)



        compo_logout = driver.find_element(By.LINK_TEXT, "Sair").click()


    finally:
        # Fecha o navegador
        print("Finalizando o programa...")