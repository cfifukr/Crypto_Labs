
from django.contrib import admin
from django.urls import path
from El_Gamal import views as viewsGamal
from elipt import views as viewsEllipt
from Shami import views as viewsShamir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',viewsRSA.main_page, name = "main_page"),

    path('el-gamal_decipher/', viewsGamal.el_gamal_decrypt_page, name= "el_gamal_decipher_page"),
    path('el-gamal_encipher/', viewsGamal.el_gamal_encrypt_page, name= "el_gamal_cipher_page"),

    path('elliptic-curves_decipher/', viewsEllipt.ellipt_decryption_page, name="elliptic_curves_decipher_page"),
    path('elliptic-curves_encipher/', viewsEllipt.ellipt_encryption_page, name="elliptic_curves_encipher_page"),

    path('shamir_decipher/', viewsShamir.shamir_decrypt, name="shamir_decipher_page"),
    path('shamir_encipher/', viewsShamir.shamir_encrypt, name="shamir_encipher_page"),

]
