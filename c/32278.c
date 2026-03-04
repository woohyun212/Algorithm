#include <stdio.h>
#include <math.h>

int main(void)
{
    long long n;
    scanf("%lld", &n);
    if (n >= -pow(2, 15) && n <= pow(2, 15)-1)printf("short");
    else if (n >= -pow(2, 31) && n <= pow(2, 31)-1)printf("int");
    else if (n >= -pow(2, 63) && n <= pow(2, 63)-1)printf("long long");
    return 0;
}
