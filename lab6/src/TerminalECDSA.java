import java.security.KeyPair;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.util.Arrays;
import java.util.Scanner;

public class TerminalECDSA {


    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        KeyPair keyPair = SignatureECDSA.generateKeyPair();



        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();
        System.out.println("Input message");
        String message = sc.nextLine();

        byte[] signature = SignatureECDSA.sign(message, privateKey);
        boolean isVerified = SignatureECDSA.verify(message, signature, publicKey);

        System.out.println("Message: " + message);
        System.out.println("Signature: " + SignatureECDSA.bytesToHex(signature));
        System.out.println("Verified: " + isVerified);
    }
}
