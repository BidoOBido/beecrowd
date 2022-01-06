import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
   public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		while (teclado.hasNextInt()) {
			Integer n = teclado.nextInt();
			Integer[] v = new Integer[n];
		
			for (int i = 0; i < v.length; i++) {
				v[i] = teclado.nextInt();
			}
			
			Stack<Integer> monte = new Stack<>();
			monte.push(0);
			
			int aux = 0;
			long soma = 0;
			
			for (int i = 0; i < v.length; i++) {
				if ((int) monte.peek() > v[i]) {
					while (((int) monte.peek() > v[i])) {
						aux = (int) monte.pop();
						soma += aux;
						if (monte.peek() < v[i]) {
							monte.push(v[i]);
						}
					}
				} else
					monte.push(v[i]);
			}
			System.out.println(soma);
		}
		teclado.close();
	}
}
