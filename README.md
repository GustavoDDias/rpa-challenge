# rpa-challenge

#### Criar base de dados no MySQL
``` 
cd docs/database
execute o script 'script_db_rba.sql' para criar a base de dados e tabelas
```

#### ChromeDriver
``` 
Baixe o WebDrive (https://chromedriver.chromium.org/downloads) e coloque
no diretório raiz da aplicação
```

#### Instale o mysql-connector-python
``` 
no terminal de comandos digite: pip install mysql-connector-python
```

#### Instale o Selenium Python
``` 
no terminal de comandos digite: pip install selenium
```


#### Configurar arquivo de conexão com o MySQL
``` 
cd rpa-challenge.py
conn = mysql.connector.connect(host='localhost',database='db_rpa',user='root',password='')
```
