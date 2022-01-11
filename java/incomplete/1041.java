import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

     Scanner ler = new Scanner(System.in);
		double x = 0, y = 0;

		x = ler.nextDouble();
		y = ler.nextDouble();

		if (x > 0) {
			if (y > 0) {
				System.out.println("Q1");
			} else if (y < 0) {
				System.out.println("Q4");
			} else
				System.out.println("EIXO X");
		} else if (x < 0) {
			if (y > 0) {
				System.out.println("Q2");
			} else if (y < 0) {
				System.out.println("Q3");
			} else
				System.out.println("EIXO Y");
		} else
			System.out.println("Origem");

		ler.close();
    }

}
