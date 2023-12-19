import javax.crypto.KeyAgreement;

import java.security.*;
import java.util.Base64;
import java.util.Scanner;

public class DiffieHellmanDH{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        KeyPairGenerator keyPairGeneratorA = getKeyPairGenerator();
        KeyPair keyPairA = keyPairGeneratorA.generateKeyPair();

        KeyPairGenerator keyPairGeneratorB = getKeyPairGenerator();
        KeyPair keyPairB = keyPairGeneratorB.generateKeyPair();

        PublicKey publicKeyA = keyPairA.getPublic();
        System.out.println("Публічний ключ userA: " + Base64.getEncoder().encodeToString(publicKeyA.getEncoded()));

        PublicKey publicKeyB = keyPairB.getPublic();
        System.out.println("Публічний ключ userB: " + Base64.getEncoder().encodeToString(publicKeyB.getEncoded()));


        KeyAgreement keyAgreementA = getKeyAgreement(keyPairA);
        KeyAgreement keyAgreementB = getKeyAgreement(keyPairB);


        System.out.println();

        byte[] sharedSecretA = generateSharedSecret(keyAgreementA, publicKeyB);
        System.out.println("Спільний секрет userA: " + Base64.getEncoder().encodeToString(sharedSecretA));


        byte[] sharedSecretB = generateSharedSecret(keyAgreementB, publicKeyA);
        System.out.println("Спільний секрет userB: " + Base64.getEncoder().encodeToString(sharedSecretB));

        scanner.close();
    }

    private static KeyPairGenerator getKeyPairGenerator() {
        try {
            KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DH");
            keyPairGenerator.initialize(2048);
            return keyPairGenerator;
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static KeyAgreement getKeyAgreement(KeyPair keyPair) {
        try {
            KeyAgreement keyAgreement = KeyAgreement.getInstance("DH");
            keyAgreement.init(keyPair.getPrivate());

            return keyAgreement;
        } catch (NoSuchAlgorithmException | InvalidKeyException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static byte[] generateSharedSecret(KeyAgreement keyAgreement, PublicKey otherPublicKey) {
        try {
            keyAgreement.doPhase(otherPublicKey, true);
            return keyAgreement.generateSecret();
        } catch (InvalidKeyException | IllegalStateException e) {
            e.printStackTrace();
            return null;
        }
    }
}


