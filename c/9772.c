#include <stdio.h>

int main()
{
    float x, y;
    while (scanf("%f %f", &x, &y) != EOF)
    {
        if (x == 0 || y == 0)
        {
            printf("AXIS");
        }
        else if (x > 0 && y > 0)
        {
            printf("Q1");
        }
        else if (x < 0 && y > 0)
        {
            printf("Q2");
        }
        else if (x < 0 && y < 0)
        {
            printf("Q3");
        }
        else if (x > 0 && y < 0)
        {
            printf("Q4");
        }
        printf("\n");
    }
    return 0;
}
