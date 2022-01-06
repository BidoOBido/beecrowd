import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		int H1 = 0, M1 = 0, H2 = 0, M2 = 0;
		String saida = "";

		do {

			H1 = ler.nextInt();
			M1 = ler.nextInt();
			H2 = ler.nextInt();
			M2 = ler.nextInt();
			if ((H1 + H2 + M1 + M2) == 0)
				break;

			H1 = (H1 * 60) + M1;
			H2 = (H2 * 60) + M2;

			if (H1 > H2) {
				H2 += 1440;
			}

			saida += Math.abs(H2 - H1) + "\n";

		} while ((H1 + H2 + M1 + M2) != 0);

		ler.close();

		System.out.print(saida);

	}
 
}
