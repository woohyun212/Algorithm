#include <stdio.h>
#include <math.h>
int main(void)
{
    int n, k;
    scanf("%d\n%d", &n, &k);
    int sum = 0;
    for (int i = 0; i <= k; i++)
    {
        sum += n * pow(10, i);
    }
    printf("%d\n", sum);
    return 0;
}