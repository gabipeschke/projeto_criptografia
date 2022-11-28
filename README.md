# projeto_criptografia
Projeto de criptografia da cifra monoalfabética em Python

## Como executar:

1- Baixe o scrypt de criptografia (criptografia.py) e adicione em uma pasta.

2- Abra o terminal e entre na pasta que foi salva o arquivo criptografia.py

3- Crie um arquivo txt com o conteúdo que deseja criptografar ou descriptografar

3- Execute o comando:
#### python3 criptografia.py nome_arquivo.txt chave comando
  a) nome_arquivo.txt: Este é o nome do arquivo que você quer criptografar ou descriptografar. É necessário este arquivo estar dentro da pasta do projeto de criptografia (na mesma pasta de criptografia.py). Caso o scrypt não encontre o arquivo, ocorrerá um erro.
  
  b) chave : A chave deverá conter todas as 26 letras do alfabeto, sem repetições. A chave poderá estar em minúsculo, maiúsculo ou alternado. Isso não influenciará no resultado. Caso a chave não seja válida, ocorrerá um erro.
  
  c) comando : O comando pode ser ‘criptografar’ ou ‘descriptografar’. Caso seja colocado outro comando, ocorrerá um erro.
  
  
## Exemplos de entradas:

#### 1-
### Entrada:
python3 criptografia.py nome_arquivo.txt AHIJKXZNOPQRSBBCDETYLFGMUVW criptografar

Conteúdo do arquivo nome_arquivo.txt: Hello World!

### Saída:

Conteúdo do arquivo nome_arquivo_cripto.txt: Nkrrc Mctrj!

#### 2-
### Entrada:
python3 criptografia.py nome_arquivo.txt AHIJKXZNOPQRSBBCDETYLFGMUVW descriptografar

Conteúdo do arquivo nome_arquivo.txt: Nkrrc Mctrj!

### Saída:

Conteúdo do arquivo nome_arquivo_cripto.txt: Hello World!
