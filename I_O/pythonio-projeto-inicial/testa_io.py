arquivo = open("dados/contatos.csv")
arquivo_escrita = open("dados/contatos-escrita.csv", mode="w")

# print(type(arquivo.buffer))

# conteudo = arquivo.buffer.read()
# print(conteudo)

# texto_em_byte = bytes('esse é um texto em bytes', 'utf-8')
# print(texto_em_byte)

contato = "15,Verônica,veronica@veronica.com\n"
contato_bytes = bytes(contato, "utf-8")
arquivo_escrita.buffer.write(contato_bytes)

arquivo.close()
arquivo_escrita.close()