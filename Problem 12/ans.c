#include<stdio.h>

int main()
{
    long int num=1,diff=1,cnt=1,st;
    while (cnt<=500)
    {
        diff++;
        cnt=1;
        for(st=2;st<=num;st++)
            if (!(num%st))
            cnt++;
        if (cnt>500)
            break;
        num+=diff;
    }
    printf("%ld has over 500 divisors",num);
    return 0;
}
