# Criar um script que escreve dados em planilha xlsx

import openpyxl

pagina = openpyxl.Workbook()                     # Cria uma página da planilha
pagina.create_sheet('Estados')                   # Criando uma página
tarefas_page = pagina['Estados']                 # Selecionando a página
tarefas_page.append (['Estado','UF'])            # Salva como coluna na planilha
tarefas_page.append (['Minas Gerais','MG'])
tarefas_page.append (['São Paulo','SP'])
tarefas_page.append (['Rio de Janeiro','RJ'])
pagina.save('Brasil.xlsx')                         # Salva a planilha