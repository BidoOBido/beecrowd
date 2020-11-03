import java.io.IOException;
import java.io.IOException;
import java.util.Scanner; 

public class Main {
 
   public static void main(String[] args) throws IOException {

		int cont = 0, tamanho = 0, quebra = 0;

		Scanner ler = new Scanner(System.in);

		while (true) {
			tamanho = 0;
			cont = Integer.parseInt(ler.nextLine());

			if (cont == 0) {
				System.exit(0);
			}

			String[] frases = new String[cont];

			for (int i = 0; i < cont; i++) {
				frases[i] = ler.nextLine();
				frases[i] = remover(frases[i]);
				tamanho = maior(frases[i], tamanho);
			}
			quebra = quebraLinha(quebra);
			mostra(frases, tamanho);
		}
	}

	private static String remover(String ori) {
		String[] vetorString = null;
		String ajuste = "";

		ori = ori.trim();

		vetorString = ori.split("\\s+");

		for (int i = 0; i < vetorString.length; i++) {
			ajuste += vetorString[i] + " ";
		}

		return ajuste.trim();

	}

	private static int maior(String ori, int tamanho) {
		int tamFrase = ori.length();
		if (tamFrase > tamanho) {
			return tamFrase;
		} else {
			return tamanho;
		}
	}

	private static int quebraLinha(int quebra) {
		if (quebra != 0) {
			System.out.printf("\n");
			quebra++;
		} else {
			quebra++;
		}
		return quebra;
	}

	private static void mostra(String[] frase, int tamanho) {
		for (int i = 0; i < frase.length; i++) {
			System.out.print(String.format("%" + tamanho + "s\n", frase[i]));
		}

	}

}
