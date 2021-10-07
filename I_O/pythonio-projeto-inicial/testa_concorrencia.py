contato_carol = "11,Carol,carol@carol.com\n"
contato_andressa = "12,Andressa,andressa@andressa.com\n"

with open('dados/contatos-escrita.csv', mode="w") as arq1:
  arq1.write(contato_carol)
with open('dados/contatos-escrita.csv', mode="a") as arq2:
  arq2.write(contato_andressa)


# arq1.close()
# arq2.close()