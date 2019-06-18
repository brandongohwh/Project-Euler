#include<stdio.h>

int prime(int x)
{
    int a;
    if (x<0 || x==1 || x==2) //Must handle negative cases
        return 0;
    for(a=2;a<x;a++)
    {
        if (!(x%a))
            return 0;
    }
    return 1;
}

int main(){

    int n,a,b,x,max=-1,sta,stb,stn,cnt;
    for(a=-999;a<1000;a++)
    {
        for(b=-1000;b<=1000;b++)
        {
            cnt=0;
            n=0;
            while (1)
            {
                x=prime(n*n+a*n+b);
                if (x==0)
                {
                    break;
                }
                cnt++;
                n++;
            }

            if(cnt>max)
            {
                max=cnt;
                sta=a;
                stb=b;
                stn=n;
            }
        }
    }
    printf("Coefficients: (%d, %d) yield %d primes, product=%d", sta,stb,stn, sta*stb);
    return 0;
}
