#include<stdio.h>

int prime(long long int x);

int main()
{
    long long int div=2,max=0,cur,num=600851475143;
    int a;
    cur=num;
    while(cur!=1)
    {
        if (!(cur%div))
        {
            if (prime(div))
                if (div>max)
                    max=div;
            cur/=div;
            div=2;
            continue;
        }
        div++;
    }
    printf("Largest prime factor of %lld is: %lld",num,max);
    return 0;
}

int prime(long long int x)
{
    long int a;
    for(a=2;a<x;a++)
        if (!(x%a))
            return 0;
    return 1;
}
