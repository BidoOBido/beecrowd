import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
   Scanner ler = new Scanner(System.in);
		double x = 0, y = 0;

		x = ler.nextDouble();
		y = ler.nextDouble();

		if (x == 0) {
			if (y == 0)
				System.out.println("Origem");
			else
				System.out.println("Eixo Y");
		} else if (x > 0) {
			if (y == 0) {
				System.out.println("Eixo X");
			} else if (y > 0)
				System.out.println("Q1");
			else
				System.out.println("Q4");
		} else if (x < 0) {
			if (y == 0) {
				System.out.println("Eixo X");
			} else if (y > 0)
				System.out.println("Q2");
			else
				System.out.println("Q3");

			ler.close();
		}
 
    }
 
}
