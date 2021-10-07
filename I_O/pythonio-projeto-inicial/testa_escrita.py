arquivo = open("dados/contatos-escrita.csv", mode="a+")

contatos = [ "11,Carol,carol@carol.com\n",
                  "12,Ana,ana@ana.com\n",
                  "13,Tais,tais@tais.com\n" ]

for contato in contatos:
  arquivo.write(contato)

arquivo.flush()

arquivo.seek(28)
arquivo.write("12,Ana,ana@ana.com\n".upper())

arquivo.flush()
arquivo.seek(0)

for c in arquivo:
  print(c, end="")
