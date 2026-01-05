import random

print('='*30)
print('{:^30}'.format('GERADOR DE SENHAS'))
print('='*30)

num_senhas = 0
while num_senhas < 1:
    num_senhas = int(input("Número de senhas: "))
    if num_senhas < 1:
       print("Ocorreu um erro na geração de senhas!")
tamanho_senha = 0

while tamanho_senha < 8:
    tamanho_senha = int(input("Quantidade de dígitos na senha: "))
    if tamanho_senha < 8:
        print("A senha deve conter pelo menos 8 dígitos.")

caracteres = ['.', '+', '-', '@', '#', '*', '!','?', '~'
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z']



def geraSenha(n_senha, t_senha):
    senhas = []
    i = 1

    while i <= n_senha:
        senha = []

        while len(senha) < t_senha:
            senha.append(random.choice(caracteres))
            if len(senha) == t_senha:
                break
        senhas.append(senha)
        i = i + 1

    return senhas


senhas_geradas = geraSenha(num_senhas, tamanho_senha)

j = 1
for senha in senhas_geradas:
    password = ''.join(senha)
    print(f'Senha {j}: {password} \n')
    j = j + 1
