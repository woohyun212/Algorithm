#include <stdio.h>
#include <string.h>

int main(void)
{
    char a[21], b[21];
    scanf("%s", a);
    scanf("%s", b);
    if (!strcmp(a, b))
        printf("0");
    else
        printf("1550");

    return 0;
}
