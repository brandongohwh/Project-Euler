#include<stdio.h>

int clean20(long long int x)
{
    int a;
    for (a=1;a<=20;a++)
        if (x%a)
            return 0;
    return 1;
}
int main()
{
    long long int a=1;
    while(1)
    {
        if (clean20(a))
            break;
        a++;}
    printf("Smallest positive number evenly divisible by 1 to 20: %lld\n", a);
    return 0;
}
