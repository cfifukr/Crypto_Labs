
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //RC4Files.saveResults("/Users/malchikmac/Desktop/Crypto_Labs/Cursova/src/resources/input.txt",
        //        "/Users/malchikmac/Desktop/Crypto_Labs/Cursova/src/resources/output.txt",
        //        "hello");

        //RC4Files.saveResults("/Users/malchikmac/Desktop/Crypto_Labs/Cursova/src/resources/output.txt",
        //        "/Users/malchikmac/Desktop/Crypto_Labs/Cursova/src/resources/output2.txt",
        //        "hello");

        Scanner sc = new Scanner(System.in);
        int counter = 0;

        System.out.println("Algorithms: ");
        for (Algorithm i : Algorithm.values()){
            counter += 1;
            System.out.println(i + " - " + counter);
        }

        System.out.println("Choose algorithm");

        if( Integer.parseInt(sc.nextLine()) == 1) {


            System.out.println("Input full path of input file");
            String inputPath = sc.nextLine();

            System.out.println("Input full path of output file");
            String outputPath = sc.nextLine();

            System.out.println("Input key");
            String key = sc.nextLine();

            RC4Files.saveResults(inputPath, outputPath, key);
        }else{
            System.out.println("My programm doesnt implements this an algorithm");
        }


    }
}