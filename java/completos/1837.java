import java.io.IOException;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
  public static void main(String[] args) throws IOException {

		int a, b, q, r;

		Scanner ler = new Scanner(System.in);

		a = ler.nextInt();
		b = ler.nextInt();

		q = a / b;
		r = a % b;

		if (a < 0 && b < 0) {
			if (r < 0 && q <= 0) {
				q++;
				r = -(b * q) + a;
			} else if (r < 0 && q > 0) {
				q++;
				r = -(b * q) + a;
			}

		} else {
			if (r < 0 && q <= 0) {
				q--;
				r = -(b * q) + a;
			} else if (r < 0 && q > 0) {
				q++;
				r = -(b * q) + a;
			}
		}

		System.out.println(q + " " + r);
		ler.close();

	}
	
}
