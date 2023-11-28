import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class RC4Files {

    public static void saveResults(String inputFilePath, String outputFilePath, String key){
        try {
            byte[] inputBytes = readFile(inputFilePath);

            RC4 rc4 = new RC4(key.getBytes());


            byte[] resultBytes = rc4.crypt(inputBytes);

            writeFile(outputFilePath, resultBytes);

            System.out.println("File successfully encrypted/decrypted.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static byte[] readFile(String filePath) throws IOException {
        try (FileInputStream fis = new FileInputStream(filePath)) {
            byte[] content = new byte[fis.available()];
            fis.read(content);
            return content;
        }
    }

    private static void writeFile(String filePath, byte[] content) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filePath)) {
            fos.write(content);
        }
    }
}