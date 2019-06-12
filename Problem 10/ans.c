#include<stdio.h>

int prime(long long int x)
{
    int a;
    for(a=2;a<x;a++)
        if (!(x%a))
            return 0;
    return 1;
}

int main()
{
    long long int sum=0,a;
    for (a=2;a<2000000;a++)
        if (prime(a))
               sum+=a;
    printf("Sum of primes <20000000: %lld",sum);
    return 0;
}
