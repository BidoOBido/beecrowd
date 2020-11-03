import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
      	Scanner ler = new Scanner(System.in);
		int n, l, m2 = 0, m3 = 0, m4 = 0, m5 = 0;

		n = ler.nextInt();
		for (int i = 1; i <= n; i++) {
			l = ler.nextInt();
			if (l % 2 == 0)
				m2++;
			if (l % 3 == 0)
				m3++;
			if (l % 4 == 0)
				m4++;
			if (l % 5 == 0)
				m5++;
		}
		System.out.println(m2 + " Multiplo(s) de 2");
		System.out.println(m3 + " Multiplo(s) de 3");
		System.out.println(m4 + " Multiplo(s) de 4");
		System.out.println(m5 + " Multiplo(s) de 5");
		ler.close();
    }
 
}
