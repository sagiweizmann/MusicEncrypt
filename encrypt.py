from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import json
import os

def generate_key():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key
    publickey = key.publickey() # pub key export for exchange
    print(key.exportKey())
    print(publickey.exportKey())
    return key

def encrypt(key,msg):
    encryptor = PKCS1_OAEP.new(key.publickey())
    encrypted = encryptor.encrypt(bytes(msg, 'utf8'))
    print(encrypted)
    #message to encrypt is in the above line 'encrypt this message'

def get_data():
    if (os.path.exists("./data_file.json")):
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
        read_file.close()
    else:
        data = {"admin": "admin"}
    return data
def main():
    data = get_data()
    name='mar'
    if (dict(data).get(name) != None):
        print("Try again")
    else:
        pub=generate_key()
        temp=str(pub.publickey().exportKey().decode())
        pas=12345
        data1 = {name: {
            'pass': pas,
            'pubkey': temp
            }
        }
        data1.update(data)
        with open("data_file.json", "w") as write_file:
            json.dump(data1, write_file)
        write_file.close()
        msg="hello word"
        encrypt(pub,msg)



main()