import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner ler = new Scanner(System.in);

		int testes = ler.nextInt();
		String saida = "";

		for (long i = 0; i < testes; i++) {
			int tam = 0;
			String a = ler.next();
			String b = ler.next();

			for (long j = 0; j < a.length(); j++) {
				if (a.charAt((int) j) > a.charAt((int) j))
					tam += conta(b.charAt((int) j), a.charAt((int) j));
				else
					tam += conta(a.charAt((int) j), b.charAt((int) j));
			}

			saida += tam + "\n";

		}

		System.out.print(saida);
		ler.close();
	}

	private static int conta(char a, char b) {
		int cont = 0;

		if (a == b)
			return 0;

		do {
			a++;
			cont++;

			if (a > 'z')
				a = 'a';

		} while (a != b);

		return cont;
	}

}
