import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
 
Scanner ler = new Scanner(System.in);
		int n, voltas;
		String str1, str2, frase = "";

		n = ler.nextInt();
		for (int i = 0; i < n; i++) {
			frase = "";
			str1 = ler.next();
			str2 = ler.next();

			if (str1.length() < str2.length())
				voltas = str2.length();
			else
				voltas = str1.length();

			for (int j = 0; j < voltas; j++) {
				if (j < str1.length()) {
					frase += str1.charAt(j);
				}

				if (j < str2.length()) {
					frase += str2.charAt(j);
				}
			}
			System.out.println(frase);
		}

		ler.close();
 
    }
 
}
