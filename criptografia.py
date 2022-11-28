import sys
import os.path

LETTERS_ALLOWED = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# criptografa ou descriptografa o conteudo da lista de strings
def crypt(content, key, encrypt):
    newContent = ''
    for line in content:
        newContent += cryptLine(line, key, encrypt)
    
    return newContent

# criptografa ou descriptografa uma string
def cryptLine(line, key, encrypt):
    newLine = ''
    for char in line:
        charIsLower = char.islower()
        if char.upper() in LETTERS_ALLOWED:
            newChar = cryptLetter(char.upper(), key, encrypt)
            newLine += ajustCase(newChar, charIsLower)
        else:
            newLine += ajustCase(char, charIsLower)

    return newLine

# criptografa ou descriptografa uma string
def cryptLetter(char, key, encrypt):
    if encrypt:
        positionChar = LETTERS_ALLOWED.rfind(char)
        return key[positionChar]
    else:
        positionChar = key.upper().rfind(char.upper())
        return LETTERS_ALLOWED[positionChar]

# ajusta o case na letra, para upper ou lower
def ajustCase(char, isLower):
    if isLower:
        return char.lower()
    
    return char.upper()

# verifica se a chave é válida
def checkValidKey(key):
    keyLegth = 26

    if len(key) != keyLegth:
        return False

    charArrayKey = list(key.upper())

    charArrayKeySorted = sorted(charArrayKey)

    stringKeySorted = ""

    for char in charArrayKeySorted:
        stringKeySorted += char

    if not stringKeySorted.__eq__(LETTERS_ALLOWED):
        return False

    return True

# a partir do nome antigo, cria um novo nome para o arquivo de retorno
def createNewFileName(fileName):
    splitedFileName = fileName.split('.')
    newFileName = splitedFileName[0] + '_cripto'

    if len(splitedFileName) > 1:
        newFileName = newFileName + '.' + splitedFileName[1]
        

    return newFileName
    

# tenta ler o txt e retorna uma lista de strings com seu conteúdo de cada linha
def readFile(fileName):
    if not os.path.isfile(fileName):
        raise Exception('O arquivo não existe')
    else:
        with open(fileName) as file:
            content = file.readlines()
            return content

# cria um arquivo de texto com o resultado da criptografia ou descriptografia
def writeFile(content, fileName):
    with open(fileName, 'w') as file:
            file.write("".join(content))
    

def main():
    #leitura de dados
    try:
        fileName = sys.argv[1]
        key = sys.argv[2].lower()
        command = sys.argv[3].lower()
    except:
        raise Exception('Execute o scrypt passando todos os comandos necessários')

    if not checkValidKey(key):
        raise Exception('Chave inválida!')

    content = readFile(fileName)
    
    if command == 'criptografar':
        content = crypt(content, key, True)
    elif command == 'descriptografar':
        content = crypt(content, key, False)
    else:
        raise Exception(f"'{command}': comando inválido")

    newFileName = createNewFileName(fileName)

    writeFile(content, newFileName)
    

    print(f"Ação '{command}' realizada com sucesso!")
    print(f"Acesse o resultado no arquivo {newFileName}")
        

if __name__ == '__main__':
    main()
