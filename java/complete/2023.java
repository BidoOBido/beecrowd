import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		HashMap<String, String> listaOriginal = new HashMap<String, String>();
		ArrayList<String> listaOrdenada = new ArrayList<String>();
		Integer iCount = 0;

		while (ler.hasNextLine()) {
			String lido = ler.nextLine();

			listaOriginal.put(lido.toUpperCase(), lido);
			listaOrdenada.add(lido.toUpperCase());

		}

		Collections.sort(listaOrdenada);

		System.out.println(listaOriginal.get(listaOrdenada.get(listaOrdenada.size() - 1)));

	}

}
