#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char a[3], b[3];
    scanf("%s %s", a, b);
    const long c = strtol(a, NULL, 10);
    const long d = strtol(b, NULL, 10);
    printf("%ld", (c - 9) * 60 + d);
    return 0;
}
