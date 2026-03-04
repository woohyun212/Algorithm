#include <stdio.h>

int main(void)
{
    int antenna,eyes=0;
    scanf("%d\n%d", &antenna, &eyes);
    if (antenna>=3&&eyes<=4)
    {
        printf("TroyMartian\n");
    }
    if (antenna<=6&&eyes>=2)
    {
        printf("VladSaturnian\n");
    }
    if (antenna<=2&&eyes<=3)
    {
        printf("GraemeMercurian");
    }
    return 0;
}
