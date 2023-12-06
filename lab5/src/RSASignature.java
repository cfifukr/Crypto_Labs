import java.security.*;
import java.util.Base64;
import java.util.Scanner;

public class RSASignature {
    private PrivateKey privateKey;
    private PublicKey publicKey;

    public RSASignature(int keySize) throws NoSuchAlgorithmException {
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(keySize);
        KeyPair keyPair = keyPairGenerator.generateKeyPair();
        this.privateKey = keyPair.getPrivate();
        this.publicKey = keyPair.getPublic();
    }

    public String signMessage(String message) throws Exception {
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initSign(privateKey);
        signature.update(message.getBytes());

        byte[] signedBytes = signature.sign();
        return Base64.getEncoder().encodeToString(signedBytes);
    }

    public boolean verifySignature(String message, String signature) throws Exception {
        Signature verifier = Signature.getInstance("SHA256withRSA");
        verifier.initVerify(publicKey);
        verifier.update(message.getBytes());

        byte[] signatureBytes = Base64.getDecoder().decode(signature);

        return verifier.verify(signatureBytes);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введіть розмір ключа (512, 1024 або 2048 біт): ");
        int keySize = scanner.nextInt();
        scanner.nextLine();

        try {
            RSASignature rsaSignature = new RSASignature(keySize);

            System.out.print("Введіть повідомлення: ");
            String message = scanner.nextLine();

            String signature = rsaSignature.signMessage(message);
            System.out.println("Електронно-цифровий підпис: " + signature);

            System.out.print("Бажаєте перевірити підпис? (так/ні): ");
            String verifyInput = scanner.nextLine();
            if (verifyInput.toLowerCase().equals("так")) {


                //RSASignature rsaSignatureTest = new RSASignature(1024);
                //String signature1 = rsaSignatureTest.signMessage(message + "324");


                boolean isVerified = rsaSignature.verifySignature(message, signature);
                if (isVerified) {
                    System.out.println("Підпис перевірений.");
                } else {
                    System.out.println("Підпис не перевірений.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}