#include <stdio.h>
#include <math.h>

int main(void)
{
    float diameter, time = 0; // inch, sec
    int rotate = 0;
    for (int i = 1;; i++)
    {
        scanf("%f %d %f", &diameter, &rotate, &time);
        if (rotate == 0)break;
        float distance = diameter * M_PI * rotate / 63360; // mile
        float mph= distance / (time / 3600); // mile/hr
        printf("Trip #%d: %.2f %.2f\n", i, distance, mph);
    }

    return 0;
}
