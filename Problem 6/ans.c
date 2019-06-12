#include<stdio.h>

int main()
{
    long long int sqs=0,ssq=0;
    int a;
    for (a=1;a<=100;a++)
    {
        sqs+=(a*a);
        ssq+=a;
    }
    ssq*=ssq;
    if (ssq>sqs)
        printf("Difference between first hundred natural numbers: %lld",ssq-sqs);
    else
            printf("Difference between first hundred natural numbers: %lld",sqs-ssq);
    return 0;
}
