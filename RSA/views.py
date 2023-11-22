from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import FileUploadForm
import os
import sympy

class rsa_functions:
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = rsa_functions.extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def mod_inverse(a, m):
        g, x, y = rsa_functions.extended_gcd(a, m)
        if g != 1:
            raise Exception('Оберненого числа не існує')
        else:
            return x % m

def main_page(request):
    return render(request, "rsa/main.html")

@csrf_exempt
def RSA_cipher_page(request):

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():

            uploaded_files = form.save()

            input_file_path = uploaded_files.input_file.path
            output_file_path = uploaded_files.output_file.path
            input_file_name = os.path.basename(input_file_path)
            output_file_name = os.path.basename(output_file_path)

            with open(input_file_path, 'r') as file:
                content_input = file.read()

            with open(output_file_path, 'r') as file:
                content_output = file.read()

            p = int(request.POST["pvalue"])
            q = int(request.POST["qvalue"])
            e = int(request.POST["evalue"])
            n = p * q
            message = content_input
            m = int.from_bytes(message.encode(), byteorder='big')
            c = pow(m, e, n)

            with open(output_file_path, 'wb') as file:
                file.write(c.to_bytes((c.bit_length() + 7) // 8, byteorder='big'))
            return redirect("main_page")
        else:
            form = FileUploadForm()
            return render(request, 'rsa/RSA_encipher.html', {'form': form})

    else:
        form = FileUploadForm()
        return render(request, 'rsa/RSA_encipher.html', {'form': form})


@csrf_exempt
def RSA_decipher_page(request):

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = form.save()

            input_file_path = uploaded_files.input_file.path
            output_file_path = uploaded_files.output_file.path
            input_file_name = os.path.basename(input_file_path)
            output_file_name = os.path.basename(output_file_path)

            with open(input_file_path, 'r') as file:
                content_input = file.read()

            with open(output_file_path, 'r') as file:
                content_output = file.read()

            p = int(request.POST["pvalue"])
            q = int(request.POST["qvalue"])
            e = int(request.POST["evalue"])
            n = p * q
            # Виконуємо дешифрування (m = c^d mod n)
            d = rsa_functions.mod_inverse(e, (p - 1) * (q - 1))

            # Зчитуємо зашифрований текст з вхідного файлу
            with open(input_file_path, 'rb') as f:
                message = int.from_bytes(f.read(), byteorder='big')
                print(input_file_path)


            m = pow(message, d, n)
            decrypted_message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
            with open(output_file_path, 'w') as file:
                file.write(decrypted_message)
                print(output_file_path)
            return redirect("main_page")
        else:
            form = FileUploadForm()
            return render(request, 'rsa/RSA_decipher.html', {'form': form})

    else:
        form = FileUploadForm()
        return render(request, 'rsa/RSA_decipher.html', {'form': form})