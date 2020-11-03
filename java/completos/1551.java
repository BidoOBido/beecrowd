import java.io.IOException;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		int n, cont, c = 0;
		String frase;
		n = ler.nextInt();
		ler.nextLine();
		for (cont = 0; cont < n; cont++) {
			frase = ler.nextLine();
			for (int j = 97; j < 123; j++) {
				for (int i = 0; i < frase.length(); i++) {
					if (frase.charAt(i) == j) {
						c++;
						break;
					}
				}
			}
			if(c==26)
			System.out.println("frase completa");
			else if(c>=13)
				System.out.println("frase quase completa");
			else
				System.out.println("frase mal elaborada");
			c=0;
		}
	}
}


