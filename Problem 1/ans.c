#include <stdio.h>

int main()
{
    int a,sum=0;
    for (a=0;a<1000;a++)
        if ((!(a%3))||(!(a%5)))
            sum+=a;
    printf("Sum of multiples of 3 OR 5 below 1000: %d\n",sum);
}
