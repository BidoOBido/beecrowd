import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
		Scanner ler = new Scanner(System.in);
		int n;
		double n1, n2, n3;
		double[] m;

		n = ler.nextInt();
		m = new double[n];

		for (int i = 0; i < n; i++) {

			n1 = ler.nextDouble();
			n2 = ler.nextDouble();
			n3 = ler.nextDouble();

			m[i] = ((n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5));
		}

		for (int j = 0; j < n; j++) {
			System.out.printf("%.1f\n", m[j]);
		}
		ler.close(); 
    }
 
}
