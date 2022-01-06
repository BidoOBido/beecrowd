import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner ler = new Scanner(System.in);
		Integer iTeste, iGol, golB = 0, golR = 0, golG = 0;
		String timeA, timeB;
		String saida = "";

		iTeste = ler.nextInt();

		for (int i = 0; i < iTeste; i++) {
			golB = 0;
			golR = 0;
			golG = 0;
			iGol = ler.nextInt();
			for (int j = 0; j < iGol; j++) {
				timeA = ler.next();
				timeB = ler.next();

				switch (timeA) {
				case "B":
					golB += valorGol(timeA, timeB);
					break;
				case "R":
					golR += valorGol(timeA, timeB);
					break;
				case "G":
					golG += valorGol(timeA, timeB);
					break;
				}
			}
			saida += mostra(golB, golR, golG) + "\n";
		}

		System.out.print(saida);

	}

	public static int valorGol(String A, String B) {
		switch (A) {
		case "B":
			if (B.equals("G"))
				return 1;
			else
				return 2;
		case "R":
			if (B.equals("B"))
				return 1;
			else
				return 2;
		case "G":
			if (B.equals("R"))
				return 1;
			else
				return 2;

		default:
			return 0;
		}
	}

	public static String mostra(Integer golB, Integer golR, Integer golG) {
		if ((golB == golR) && (golR == golG)) {
			return "trempate";
		} else if (((golB == golR) && (golB > golG)) || ((golR == golG) && (golR > golB))
				|| ((golG == golB)) && (golG > golR)) {
			return "empate";
		} else {
			if ((golB > golR) && (golB > golG)) {
				return "blue";
			} else if ((golR > golB) && (golR > golG)) {
				return "red";
			} else if ((golG > golB) && (golG > golR)) {
				return "green";
			}
		}
		return "";

	}

}
