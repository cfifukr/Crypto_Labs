import java.util.Arrays;
import java.util.Scanner;

public class Test {
    public static void main(String[] args){
        String key = "EBELe8UfuoIaQn0k1nU0oQ==";

        RC4 test = new RC4(key.getBytes());
        String text = "Vladyslav";
        byte[] cipher = test.crypt(text.getBytes());
        String cipherText = new String(cipher).substring(1); //шифротекст без першого елементу


        System.out.println("Не пошкоджений шифр");
        test.reset(key.getBytes());
        byte[] decipher = test.crypt(cipher);
        System.out.println(new String(decipher));


        System.out.println("Пошкоджений шифр(без першого символу)");
        test.reset(key.getBytes());
        byte[] decipher2 = test.crypt(cipherText.getBytes());
        System.out.println(new String(decipher2));



    }
}
