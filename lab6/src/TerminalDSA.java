import java.security.KeyPair;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.util.Scanner;

public class TerminalDSA {
    static Scanner sc = new Scanner(System.in);


    public static void main(String[] args) throws Exception {
        KeyPair keyPair = SignatureDSA.generateKeyPair();

        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();
        //System.out.println(privateKey);
        //System.out.println(publicKey);


        System.out.println("Input message");
        String message = sc.nextLine();

        byte[] signature = SignatureDSA.sign(message, privateKey);




        boolean isVerified = SignatureDSA.verify(message, signature, publicKey);

        System.out.println("Message: " + message);
        System.out.println("Signature: " + SignatureDSA.bytesToHex(signature));
        System.out.println("Verified: " + isVerified);
    }



}
