#include<stdio.h>

int main()
{
    int a,b,c;
    for(c=0;c<=1000;c++)
        for(b=0;b<c;b++)
            for(a=0;a<b;a++)
                if (a+b+c==1000 && c*c==a*a+b*b)
                    printf("Product: %d, a: %d, b: %d, c: %d", a*b*c,a,b,c);
    return 0;
}
