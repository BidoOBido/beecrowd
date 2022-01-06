import java.io.IOException;
import java.util.Scanner;

public class Main {
 
   public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		int cont = 0, soma = 0;
		double media;

		while (ler.hasNextLine()) {
			ler.nextLine();
			cont++;
			soma += Integer.parseInt(ler.nextLine());
		} 

		media = (double) soma / cont;

		System.out.printf("%.1f\n", media);

		ler.close();
	}
 
}
