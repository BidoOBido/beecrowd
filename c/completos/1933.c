#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b;

  scanf("%d", &a);
  scanf("%d", &b);

  if (a < b) printf("%d\n", b);
  else printf("%d\n", a);

  return 0;
}
