from hashlib import md5, sha256, sha224, sha384, sha1

def getHashfromfile(file):
    hash0 = sha256()
    b = bytearray(128*1024)
    mv = memoryview(b)
    
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            hash0.update(mv[:n])
            return hash0.hexdigest()
  
hash0 = getHashfromfile("pato.txt")
print("")
print ("Criptografia em sha256: ", hash0)
print("")
######################################################################################################

def getHashfromfile(file):
    hash1 = md5()
    b1 = bytearray(128*1024)
    mv1 = memoryview(b1)
    
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv1), 0):
            hash1.update(mv1[:n])
            return hash1.hexdigest()
        

hash1 = getHashfromfile("pato.txt")
print ("Criptografia em md5: ", hash1)
print("")

######################################################################################################

def getHashfromfile(file):
    hash2 = sha224()
    b2 = bytearray(128*1024)
    mv2 = memoryview(b2)
    
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv2), 0):
            hash2.update(mv2[:n])
            return hash2.hexdigest()
       
hash2 = getHashfromfile("pato.txt")
print ("Criptografia em sha224: ", hash2)
print("")
        
#####################################################################################################

def getHashfromfile(file):
    hash3 = sha384()
    b3 = bytearray(128*1024)
    mv3 = memoryview(b3)
    
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv3), 0):
            hash3.update(mv3[:n])
            return hash3.hexdigest()
       
hash3 = getHashfromfile("pato.txt")
print ("Criptografia em sha384: ", hash3)
print("")

######################################################################################################

def getHashfromfile(file):
    hash4 = sha1()
    b4 = bytearray(128*1024)
    mv4 = memoryview(b4)
    
    with open(file, "rb", buffering=0) as f:
        for n in iter(lambda : f.readinto(mv4), 0):
            hash4.update(mv4[:n])
            return hash4.hexdigest()
       
hash4 = getHashfromfile("pato.txt")
print ("Criptografia em sha1: ", hash4)
print("")

# Descriptografia 

import hashlib
import string
import itertools

def md5_hash(hash1):
    
    return hashlib.md5(hash1.encode()).hexdigest()

def brute_force_md5(hash_to_crack, length=10):
    
    characters = string.ascii_lowercase + string.digits  
    for length in range(1, length + 1): 
        for attempt in itertools.product(characters, repeat=length):
            candidate = ''.join(attempt)
            if md5_hash(candidate) == hash_to_crack:
                return candidate
    return None


if __name__ == "__main__":
    
    hash_md5 = hash1  
    
    result = brute_force_md5(hash_md5, length=10)  
    if result:
        print(f"Esse hash significa: {result}")
    else:
        print("Deu não man")
print ("")
