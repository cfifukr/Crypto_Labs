from django.shortcuts import render
import os
import base64

def encrypt_message(public_key, message):
    ciphertext = b""
    iv = os.urandom(16)


    return base64.b64encode(iv + ciphertext)

def decrypt_message(private_key, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    return ciphertext
def ellipt_encryption_page(request):


    return render(request, 'ellipt/elliptic_curves_encryption.html')


def ellipt_decryption_page(request):


    return render(request, 'ellipt/elliptic_curves_decryption.html')

