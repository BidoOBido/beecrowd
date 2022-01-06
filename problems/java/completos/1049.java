import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
Scanner ler = new Scanner(System.in);
		String c1, c2, c3;

		c1 = ler.nextLine();
		c2 = ler.nextLine();
		c3 = ler.nextLine();

		if (c1.equals("vertebrado")) {
			if (c2.equals("ave")) {
				if (c3.equals("carnivoro"))
					System.out.println("aguia");
				else
					System.out.println("pomba");
			} else {
				if (c3.equals("onivoro"))
					System.out.println("homem");
				else 
					System.out.println("vaca");
			}

		} else {
			if (c2.equals("inseto")) {
				if (c3.equals("hematofago"))
					System.out.println("pulga");
				else
					System.out.println("lagarta");
			} else {
				if (c3.equals("hematofago"))
					System.out.println("sanguessuga");
				else
					System.out.println("minhoca");
			}
		}

		ler.close();
    }
 
}
