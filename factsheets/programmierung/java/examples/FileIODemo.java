import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileIODemo {
    public static void main(String[] args) {
        String filename = "test.txt";

        try (FileWriter writer = new FileWriter(filename)) {
            writer.write("Hello Java IO!");
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line = reader.readLine();
            System.out.println("Read from file: " + line);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
