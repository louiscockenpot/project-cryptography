import hashlib

def verify_signature(p, g, y, r, s, m):
    left_side = pow(g, m, p)     
    print("left_side: ", left_side)
    right_side = (pow(y, r, p) * pow(r, s, p)) % p 
    print("right_side: ", right_side)
    
    return left_side == right_side, left_side, right_side


def encrypt_text(M):
    H_Texte=hashlib.sha256(M.encode('utf-8'))
    N_Texte=int(H_Texte.hexdigest(),base=16) % (2**54)
    
    return N_Texte


def verify(message, signature, public_key):
    
    message_H = encrypt_text(message)
    r, s = signature
    p, g, A = public_key

    authentic = verify_signature(p, g, A, r, s, message_H)

    return authentic
