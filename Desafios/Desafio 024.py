#leia o nome de uma cidade e veja se ela começa com o nome 'Santo'
cidade=str(input('Digite o nome da sua cidade: ')).strip()
n=cidade.split()
if n[0] == "Santo":
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
    