#include<stdio.h>

int main()
{
    long int a,maxint;
    long long int x;
    int b,max=0;

    for (a=1; a<1000000; a++)
    {
        b=0;
        x=a;
        while (x!=1)
        {
            if (x%2)
            {
                x=x*3+1;
            }
            else
            {
                x/=2;
            }
            b++;
        }
        if (max<b)
        {
            max=b;
            maxint=a;
        }
    }
    printf("Starting number %ld produces the longest chain of length %ld\n", maxint,max);
    return 0;
}
