import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.security.NoSuchAlgorithmException;

public class Main {

    public static SecretKey generateSymmetricKey() throws NoSuchAlgorithmException {


        KeyGenerator keyGenerator = KeyGenerator.getInstance("RC4");
        keyGenerator.init(128);

        SecretKey secretKey = keyGenerator.generateKey();

        return secretKey;
    }

    public static void main(String[] args) {
        try {
            SecretKey symmetricKey = generateSymmetricKey();

            byte[] keyBytes = symmetricKey.getEncoded();

            System.out.println("ключ : " + java.util.Base64.getEncoder().encodeToString(keyBytes));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}