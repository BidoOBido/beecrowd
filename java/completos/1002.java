import java.io.IOException;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
		Scanner ler = new Scanner(System.in);
		double area, raio, pi = 3.14159;

		raio = ler.nextDouble();
		area = pi * (Math.pow(raio, 2.0));
		System.out.printf("A=%.4f\n", area);

		ler.close();
 
    }
 
}