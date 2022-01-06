import java.util.Scanner;

public class Main {

	enum LED {

		N0(6), N1(2), N2(5), N3(5), N4(4), N5(5), N6(6), N7(3), N8(7), N9(6);

		int value;

		LED(int value) {
			this.value = value;
		}
		
	};

	public static void main(String[] args) {

		Scanner entrada = new Scanner(System.in);

		String saida = "";
		int quantidade = 0;
		
		int loop = Integer.valueOf(entrada.nextLine());
			
		for (int index = 0; index < loop; index++) {
			
			String valor = entrada.nextLine();
						
			for (int i = 0; i < valor.length(); i++) {
						
				quantidade += LED.values()[Character.getNumericValue(valor.charAt(i))].value;
				
			}
			
			saida += quantidade + " leds" + "\n";
			
			quantidade = 0;

		}

		entrada.close();
		
		System.out.print(saida);

	}

}
