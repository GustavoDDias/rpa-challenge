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