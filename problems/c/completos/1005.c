#include <stdio.h>
 
int main() {
 
    double A,B,MEDIA;

    scanf("%lf",&A);
    scanf("%lf",&B);

    MEDIA = ((A*.35)+(B*.75))*(1/1.1);

    printf("MEDIA = %.5lf\n",MEDIA);
 
    return 0;
}