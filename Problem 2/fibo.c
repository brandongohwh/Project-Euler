#include<stdio.h>
#include<math.h>

int main()
{
    long int sum=0,x1=1,x2=2,x3=3;

    while(x1<=4*pow(10,6))
    {
        if (!(x1%2))
            sum+=x1;
        x1=x2;
        x2=x3;
        x3=x1+x2;
    }
    printf("Sum of even numbered Fibonacci numbers <= 4 million: %ld\n",sum);
    return 0;
}
