import time
from hashlib import md5, sha256, sha224, sha384, sha1

def delay_print(pato, delay=0.03):
   
    for char in pato:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def get_hash_from_file(file, hash_func):
   
    hash_obj = hash_func()
    b = bytearray(128*1024)
    mv = memoryview(b)
    
    with open(file, "rb", buffering=0) as f:
        while True:
            n = f.readinto(mv)
            if n == 0:
                break
            hash_obj.update(mv[:n])
    return hash_obj.hexdigest()

def print_hash(name, hash_value):
    print(f"Criptografia em {name}: ", end='')
    delay_print(hash_value)

def main():
   
    hash_functions = [(sha256, "sha256"),(md5, "md5"),(sha224, "sha224"),(sha384, "sha384"),(sha1, "sha1") ]
    
    for hash_func, name in hash_functions:
        hash_valor = get_hash_from_file("pato.txt", hash_func)
        print_hash(name, hash_valor)
    
 # Descriptografia
    import hashlib
    import string
    import itertools

    def md5_hash(hash1):
        return hashlib.md5(hash1.encode()).hexdigest()

    def brute_force_md5(hash_to_crack, length=4):
        characters = string.ascii_lowercase + string.digits  
        for length in range(1, length + 1): 
            for attempt in itertools.product(characters, repeat=length):
                candidate = ''.join(attempt)
                if md5_hash(candidate) == hash_to_crack:
                    return candidate
        return None

    hash_md5 = get_hash_from_file("pato.txt", md5)
    resultado = brute_force_md5(hash_md5, length=4)
    if resultado:
        print("")
        print(f"Esse hash significa (☞ﾟヮﾟ)☞: {resultado}")
        print("")
        
    else:
        print("Deu n man (˘･_･˘)")
        print("")

if __name__ == "__main__":
    main()
