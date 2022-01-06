import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		int n, t, f = 0, m, cont, posi;
		do {
			m = 0;
			n = ler.nextInt();
			if (n == 0)
				break;
			String[] p = new String[n];

			for (cont = 0; cont < n; cont++) {
				p[cont] = ler.next();
				t = p[cont].length();
				if (t > m)
					m = t;
			}
			if (f == 1)
				System.out.println();
			f = 1;
			for (cont = 0; cont < n; cont++) {
				t = p[cont].length();
				posi = m - t;
				for (int i = 0; i < posi; i++) {
					p[cont] = " " + p[cont];
				}
				System.out.println(p[cont]);
			}
		} while (n != 0);
	}
}
