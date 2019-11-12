# Each character on a computer is assigned a unique code and the preferred standard is ASCII 
# (American Standard Code for Information Interchange). For example, uppercase A = 65, 
# asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte 
# with a given value, taken from a secret key. The advantage with the XOR function is that using the
# same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
# then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is
# made up of random bytes. The user would keep the encrypted message and the encryption key in 
# different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a 
# password as a key. If the password is shorter than the message, which is likely, the key is repeated 
# cyclically throughout the message. The balance for this method is using a sufficiently long password 
# key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII 
# codes, and the knowledge that the plain text must contain common English words, decrypt the message 
# and find the sum of the ASCII values in the original text.
from itertools import permutations

def load_encrypted(filename):
    f = open(filename, "r")
    data = f.readline()
    f.close()

    # file looks like 36,22,80,0,0,4,23,25,19,17
    # split will keep an empty token at the front and end. Get rid of them
    codes = [int(x) for x in data.split(",")]
    print("Loaded file {0} with {1} codes".format(filename,len(codes)))
    return codes

def codes_as_string(codes,length):
    return "".join([chr(x) for x in codes[:length]])

def print_as_string(codes,length):
    print(codes_as_string(codes,length))

def is_decrypted(codes):
    dstr = codes_as_string(codes,len(codes))
    # contains "the" and " a " and no extended characters
    return "the" in dstr and " a " in dstr and min(codes) >= 32 and max(codes) <= 122

def decrypt_with_key(codes,key):
    key_val = [ord(x) for x in key]
    key_len = len(key_val)
    for i,code in enumerate(codes):
        codes[i] = code ^ key_val[i%key_len]
    return codes

codes = load_encrypted("p059_cipher.txt")
c = 0
decrypted_string = ""
for candidate_key in permutations("abcdefghijklmnopqrstuvwxyz",3):
   decrypted = decrypt_with_key(codes,candidate_key)
   if is_decrypted(decrypted):
       c += 1
       print("Found key: " + str(candidate_key))
       print_as_string(decrypted,200)
       decrypted_string = codes_as_string(decrypted,len(decrypted))
print(c)
if c == 1:
    print(sum([ord(x) for x in decrypted_string]))
