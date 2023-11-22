from django.shortcuts import render
import random
from sympy import mod_inverse

SECRET = 42

global shares
def generate_coefficients(secret, threshold, prime):
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(threshold - 1)]
    return coefficients

def evaluate_polynomial(coefficients, x, prime):
    return sum([(coeff * (x ** i)) % prime for i, coeff in enumerate(coefficients)]) % prime

def encrypt_share(secret, threshold, total_shares, prime):
    coefficients = generate_coefficients(secret, threshold, prime)
    shares = [(i, evaluate_polynomial(coefficients, i, prime)) for i in range(1, total_shares + 1)]
    return shares

def encrypt_share(secret, threshold, total_shares, prime):
    coefficients = generate_coefficients(secret, threshold, prime)
    shares = [(i, evaluate_polynomial(coefficients, i, prime)) for i in range(1, total_shares + 1)]
    return shares

def lagrange_interpolation(shares, prime):
    result = 0
    for i, share in enumerate(shares):
        xi, yi = share
        term = yi
        for j, other_share in enumerate(shares):
            if i != j:
                xj, _ = other_share
                term = (term * (0 - xj) * mod_inverse(xi - xj, prime)) % prime
        result = (result + term) % prime
    return result

def decrypt_secret(shares, prime):
    return lagrange_interpolation(shares, prime)


def shamir_encrypt(request):
    if request.method == "POST":


        p = int(request.POST["pvalue"])
        n = int(request.POST["nvalue"])
        k = int(request.POST["kvalue"])


        if k<= n:
            global shares
            shares = encrypt_share(SECRET, k, n, p)
            return render(request, "shamir/Shamir_encipher.html", {"result": shares})
        else:
            return render(request, "shamir/Shamir_encipher.html",
                          {"checkboxes_alert": "К має бути менший або рівний N " })

    else:
        return render(request, "shamir/Shamir_encipher.html")



def shamir_decrypt(request):

    if request.method == "POST":




        n = int(request.POST["nvalue"])
        k = int(request.POST["kvalue"])
        text = request.POST["text"]

        if k <= n:

            result = decrypt_secret(shares[:k], n)

            return render(request, "shamir/Shamir_decipher.html", {"result": result })
        else:
            return render(request, "shamir/Shamir_decipher.html",
                          {"checkboxes_alert": "К має бути менший або рівний N " })

    else:
        return render(request, "shamir/Shamir_decipher.html")


