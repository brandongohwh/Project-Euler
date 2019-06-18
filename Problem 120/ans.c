#include<stdio.h>

int main()
{
    long long int su=0,x,maxhi,rema,tot=0,minus,plus;
    int a,n,count;
    for (a=3; a<1001; a++)
    {
        maxhi=0;
        for (n=0; n<10000; n++)
        {
            minus=1;
            plus=1;
            for(count=0; count<n; count++)
            {
                minus=((minus)*(a-1))%(a*a);
                plus=((plus)*(a+1))%(a*a);
            }
            rema=(minus+plus)%(a*a);
            if (rema>maxhi)
                maxhi=rema;
        }
        tot+=maxhi;
    }
    printf("Sum rmax: %lld",tot);
    return 0;
}
