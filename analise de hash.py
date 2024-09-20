import hashlib
import os

def calcular_hash(arquivo_path, algoritmo='sha256'):
   
    if algoritmo not in hashlib.algorithms_available:
        raise ValueError(f"Algoritmo de hash '{algoritmo}' não suportado. Opções disponíveis: {', '.join(hashlib.algorithms_available)}")

    hash_obj = hashlib.new(algoritmo)
    try:
        with open(arquivo_path, "rb") as arquivo:
            for bloco in iter(lambda: arquivo.read(4096), b""):
                hash_obj.update(bloco)
    except IOError:
        raise IOError("Erro ao ler o arquivo. Verifique o caminho e as permissões.")
    return hash_obj.hexdigest()

def verificar_integridade(arquivo_path, hash_recebido, algoritmo='sha256'):
    
    try:
        hash_calculado = calcular_hash(arquivo_path, algoritmo)
    except ValueError as e:
        print(e)
        return False
    except IOError as e:
        print(e)
        return False
    
    
    return hash_calculado.lower() == hash_recebido.lower()

def main():
    print("")
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    print("")
    hash_recebido = input("Digite o hash recebido: ").strip()
    print("")
    algoritmo = input("Digite o algoritmo de hash: ").strip().lower()
    print("")

    if not os.path.isfile(caminho_arquivo):
        print("")
        print("Arquivo não encontrado. Verifique o caminho.")
        print("")
        return

    if verificar_integridade(caminho_arquivo, hash_recebido, algoritmo):
        print("--------------------------------------------------------------")
        print("                 O arquivo não foi alterado.                  ")
        print("--------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------")
        print("                 O arquivo foi alterado.                      ")
        print("--------------------------------------------------------------")

if __name__ == "__main__":
    main()     
