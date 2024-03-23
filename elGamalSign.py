import gmpy2
import random
import hashlib
import math

def generate_safe_prime():
    while True:
        q = gmpy2.next_prime(random.getrandbits(23))
        p = 2*q + 1
        if gmpy2.is_prime(p):
            return p, q


def find_generator(p, q):
    while True:
        g = gmpy2.mpz(random.randint(2, p - 2)) 
        if gmpy2.powmod(g, 2, p) != 1 and gmpy2.powmod(g, q, p) != 1:
            return g
        

def generate_key_pair(prime, g):
    private_key = gmpy2.mpz(random.randint(1, prime - 2))
    public_key = gmpy2.powmod(g, private_key, prime)
    return private_key, public_key


def encrypt_text(M):
    H_Texte=hashlib.sha256(M.encode('utf-8'))
    N_Texte=int(H_Texte.hexdigest(),base=16) % (2**54)
    
    return N_Texte


def signature(prime, g, private_key, m):
    while True:
        k = random.randint(2, prime - 2)
        if math.gcd(k, prime - 1) == 1:
            break

    r=pow(g,k,prime)
    kI=pow(k,-1,prime-1)

    s=((m-private_key*r)*kI) % (prime-1)
    
    return r, s


def sign(message):
    # Generate safe prime
    prime, q = generate_safe_prime()
    
    # Find generator
    g = find_generator(prime, q)
    
    # Generate key pair
    private_key, public_key = generate_key_pair(prime, g)
    
    # Encrypt text    
    encrypted_message = encrypt_text(message)
    
    # Sign the encrypted message
    r, s = signature(prime, g, private_key, encrypted_message)
    
    return int(prime), int(g), int(public_key), int(r), int(s)

    # Print the results   
    print(encrypted_message)
    print("Public key (p,g,A):", prime, g, public_key)
    print(f"Signed message to send [M,s(M)] : [{message}, ({r}, {s})]")
