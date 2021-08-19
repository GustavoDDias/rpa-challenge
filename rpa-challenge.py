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

  # inserindo os dados nos inputs do formulário
  for coluna in tabela:

    # nome
    nome = coluna[0]
    driver.find_element_by_id("name").send_keys(nome)
    time.sleep(0.5)

    # email
    email = coluna[4]
    driver.find_element_by_id("email").send_keys(email)
    time.sleep(0.5)

    # cep
    cep = coluna[3]
    driver.find_element_by_id("cep").send_keys(cep)
    time.sleep(0.5)

    # estado
    estado = coluna[2]
    driver.find_element_by_id("estado").send_keys(estado)
    time.sleep(0.5)

    # cidade
    cidade = coluna[1]
    driver.find_element_by_id("cidade").send_keys(cidade)
    time.sleep(0.5)

    # assunto
    assunto = coluna[6]
    driver.find_element_by_id("assunto").send_keys(assunto)
    time.sleep(0.5)

    # telefone 
    telefone = coluna[5]
    driver.find_element_by_id("telefone").send_keys(telefone)
    time.sleep(0.5)

    # mensagem  
    mensagem = coluna[7] 
    driver.find_element_by_id("mensagem").send_keys(mensagem)
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