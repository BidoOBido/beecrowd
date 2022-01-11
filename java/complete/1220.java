import java.util.Locale;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int n = 1;
		int[] N = new int[1000];
		Locale.setDefault(Locale.US);
		Scanner teclado = new Scanner(System.in);
		teclado.useLocale(Locale.US);
		int inteira, real;
		double valorMaior, valorMenor;
		String strn = teclado.nextLine(); 
		n = Integer.parseInt(strn);
		while (n != 0) {
			double total = 0;
			if (n == 0) break;
			for (int i = 0; i < n; i++) {
				String str = teclado.nextLine();
				str = str.replace('.', ',');
				String valores[] = str.split(",");
				int v1 = Integer.parseInt(valores[0]);
				int v2 = Integer.parseInt(valores[1]);
				N[i] = (v1 * 100) + v2; 
				total += N[i];
			}
			total = ((double) total) / n;
			valorMenor = 0;
			valorMaior = 0;
			for (int l = 0; l < n; l++) {
				if (N[l] < total) {
					valorMenor += ((int) (total - N[l])) / 100.0;
				} else {
					valorMaior += ((int) (N[l] - total)) / 100.0;
				}
			}
			if (valorMenor > valorMaior) {
				System.out.printf("$%.2f\n", valorMenor);
			} else {
				System.out.printf("$%.2f\n", valorMaior);
			}
			String strn1 = teclado.nextLine(); 
			n = Integer.parseInt(strn1);
		}
		teclado.close();
	}
}
