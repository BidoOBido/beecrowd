#include <stdio.h>
#include <stdlib.h>

int main()
{
    double area, raio, pi = 3.14159;

    scanf("%lf", &raio);

    area = pow(raio, 2.00) * pi;

    printf("A=%.4lf\n", area);

    return 0;
}
