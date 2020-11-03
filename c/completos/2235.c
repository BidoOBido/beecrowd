#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A, B, C;
    char resposta = 'N';

    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);

    if ((A == B)||(B == C)||(C == A)){
        resposta = 'S';
    } else if (((A + B) == C)||((B + C) == A)||((C + A) == B)) {
        resposta = 'S';
    } else
        resposta = 'N';

    printf("%c\n", resposta);

  return 0;
}
