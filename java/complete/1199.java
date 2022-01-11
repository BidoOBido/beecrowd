import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
public class Main {
 
   public static void main(String[] args) throws IOException {

		// define o leitor e escritor buffer
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String linha;

		// laço de repetição
		while ((linha = br.readLine()) != null) {
			if (linha.charAt(0) == '-')
				break;

			// teste para reconhecer se é hexa ou decimal
			if (linha.length() > 2 && linha.charAt(0) == '0' && linha.charAt(1) == 'x') {
				String hexadecimal = linha.substring(2, linha.length());
				bw.write(String.valueOf(Integer.parseInt(hexadecimal, 16)));
			} else {
				bw.write("0x");
				String recebe = Integer.toHexString(Integer.parseInt(linha));
				recebe = recebe.toUpperCase();
				bw.write(recebe);
			}

			bw.write("\n");
		}

		bw.flush();

	}
 
}
