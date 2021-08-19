import csv
import time
import mysql.connector
from selenium import webdriver

# iniciando conexão com o banco de dados
try:
  conn = mysql.connector.connect(host='localhost',database='db_rpa',user='root',password='')
except mysql.connector.Error as e:
  print ("Error code:", e.errno)      
  print ("SQLSTATE value:", e.sqlstate)
  print ("Error message:", e.msg)     
  print ("Error:", e)                 
  s = str(e)
  print ("Error:", s)     

cursor = conn.cursor()

# abrindo o navegador
driver = webdriver.Chrome()
driver.get("http://seguralta.com.br/site/contato")
time.sleep(2)

# carregando os dados do arquivo .csv
with open("docs/excel/contato.csv", encoding='ISO-8859-1') as arquivo:
  tabela = csv.reader(arquivo, delimiter=';')

  # ignorar a primeira linha (cabeçalho)
  next(tabela)

  row = 0
  # inserindo os dados nos inputs do formulário
  for coluna in tabela:

    row += 1

    # nome
    if coluna[0] in (None, ""):
      print("Campo Nome não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      nome = coluna[0]
      try:
        driver.find_element_by_id("name").send_keys(nome)
      except:
        print("Falha ao inserir os dados no campo Nome do formulário de contato.") 
        break
    time.sleep(0.5)

    # email
    if coluna[4] in (None, ""):
      print("Campo Email não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      email = coluna[4]
      try: 
        driver.find_element_by_id("email").send_keys(email)
      except:
        print("Falha ao inserir os dados no campo Email do formulário de contato.")
        break
    time.sleep(0.5)

    # cep
    if coluna[3] in (None, ""):
      print("Campo Cep não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      cep = coluna[3]
      try:
        driver.find_element_by_id("cep").send_keys(cep)
      except:
        print("Falha ao inserir os dados no campo Cep do formulário de contato.")
        break
    time.sleep(0.5)

    # estado
    if coluna[2] in (None, ""):
      print("Campo Estado não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      estado = coluna[2]
      try:
        driver.find_element_by_id("estado").send_keys(estado)
      except:
        print("Falha ao inserir os dados no campo Estado do formulário de contato.")
        break
    time.sleep(0.5)

    # cidade
    if coluna[1] in (None, ""):
      print("Campo Cidade não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      cidade = coluna[1]
      try:
        driver.find_element_by_id("cidade").send_keys(cidade)
      except:
        print("Falha ao inserir os dados no campo Cidade do formulário de contato.")
        break
    time.sleep(0.5)

    # assunto
    if coluna[6] in (None, ""):
      print("Campo Assunto não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      assunto = coluna[6]
      try:
        driver.find_element_by_id("assunto").send_keys(assunto)
      except:
        print("Falha ao inserir os dados no campo Assunto do formulário de contato.")
        break
    time.sleep(0.5)

    # telefone 
    if coluna[5] in (None, ""):
      print("Campo Telefone não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      telefone = coluna[5]
      try:
        driver.find_element_by_id("telefone").send_keys(telefone)
      except:
        print("Falha ao inserir os dados no campo Telefone do formulário de contato.") 
        break
    time.sleep(0.5)

    # mensagem 
    if coluna[7] in (None, ""):
      print("Campo Mensagem não encontrado no arquivo .csv, na linha: ",row) 
      break
    else: 
      mensagem = coluna[7]
      try: 
        driver.find_element_by_id("mensagem").send_keys(mensagem)
      except:
        print("Falha ao inserir os dados no campo Mensagem do formulário de contato.") 
        break
    time.sleep(0.5)

    #submit
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(3)

    # response do envio do formulario
    response = ""
    response = driver.find_element_by_class_name("alert").text

    if (response != ""):
      sqlPessoa = "INSERT INTO pessoa (nome, cidade, estado) VALUES (%s, %s, %s)"
      valPessoa = (nome, cidade, estado)
      cursor.execute(sqlPessoa, valPessoa)

      conn.commit()

      # retornando último id do insert Pessoa
      pessoa_id = cursor.lastrowid

      sqlContato = "INSERT INTO contato (pessoa_id, email, telefone) VALUES (%s, %s, %s)"
      valContato = (pessoa_id, email, telefone)
      cursor.execute(sqlContato, valContato)

      conn.commit()

      # retornando último id do insert Contato
      contato_id = cursor.lastrowid

      sqlStatus = "INSERT INTO statusmensagemenviada (pessoa_id, contato_id, assunto, mensagemenviada, retornosite) VALUES (%s, %s, %s, %s, %s)"
      valStatus = (pessoa_id, contato_id, assunto, mensagem, response)
      cursor.execute(sqlStatus, valStatus)

      conn.commit()
    else:
      print("Formulário de contato sem resposta. Os dados não foram salvos no banco de dados.")

# encerrando serviços e a aplicação
conn.close()
driver.close()