#include<stdio.h>

int main()
{
    long long int a[21][21];
    int b,c;
    for(b=0;b<21;b++)
    {
        a[b][0]=1;
        a[0][b]=1;
    }
    for(b=1;b<21;b++)
        for(c=1;c<21;c++)
            a[b][c]=a[b-1][c]+a[b][c-1];
    printf("Number of routes: %lld",a[20][20]);
    return 0;
}
