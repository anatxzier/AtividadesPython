from Classes import*

user01 = Cadastro_user("Carlos", 23)
user01.inserir_endereco("Jundiai", "SP")

user02 = Cadastro_user("Ana Júlia", 109090)
user02.inserir_endereco("Havana", "Cuba")
print(user01.getNome())
print(user01.getIdade())
print(user01.getEndereço().getCidade())
print(user01.getEndereço().getEstado())
print("....")
print(user02.getNome())
print(user02.getIdade())
print(user02.getEndereço().getCidade())
print(user02.getEndereço().getEstado())