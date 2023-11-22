
from django.shortcuts import render
from RSA.forms import FileUploadForm

import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def generate_keypair(p):
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    h = mod_exp(g, x, p)
    return g, h, x

def encrypt(p, g, h, plaintext):
    k = random.randint(2, p - 1)
    c1 = mod_exp(g, k, p)
    s = mod_exp(h, k, p)
    c2 = []
    for i in range(len(plaintext)):
        c2.append(plaintext[i] * s % p)
    return c1, c2

def decrypt(p, x, c1, c2):
    s = mod_exp(c1, x, p)
    plaintext = []
    for i in range(len(c2)):
        plaintext.append(c2[i] * mod_exp(s, p - 2, p) % p)
    return plaintext


def el_gamal_encrypt_page(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_files = form.save()
            input_file_path = uploaded_files.input_file.path
            with open(input_file_path, 'r') as file:
                content_input = file.read().encode()


            p = int(request.POST["pvalue"])

            g, h, x = generate_keypair(p)

            c1, c2 = encrypt(p, g, h, content_input)

            return render(request, 'Gamal/Gamal_encryption.html', {'result1': c1,
                                                                   'result2': c2,
                                                                   'open_key': h,
                                                                   'close_key': x})

        else:
            form = FileUploadForm()
            return render(request, 'Gamal/Gamal_encryption.html', {'form': form})

    else:
        form = FileUploadForm()
        return render(request, 'Gamal/Gamal_encryption.html', {'form': form})

def el_gamal_decrypt_page(request):
    if request.method == 'POST':

        p = int(request.POST["pvalue"])
        x = int(request.POST["xvalue"])
        m = int(request.POST["mvalue"])
        k1 = str(request.POST["kvalue"])

        j = k1.split(', ')

        k = [int(i) for i in j]


        result = decrypt(p, x, m, k)


        res = ''.join([chr(i) for i in result])

        return render(request, 'Gamal/Gamal_decryption.html', {'result': res})



    else:
        return render(request, 'Gamal/Gamal_decryption.html')

