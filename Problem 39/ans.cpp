#include<iostream>

using namespace std;

int main()
{
    long int tot1,tot2;
    int a,b,c,p,cnt,hi=0,pmax;
    for(p=0; p<=1000; p++)
    {
        cnt=0;
        for(c=0; c<=p; c++)
            for(b=0; b<=c; b++)
                for(a=0; a<=b; a++)
                {
                    tot1=c*c;
                    tot2=a*a+b*b;
                    if (tot1==tot2 && a+b+c==p)
                        cnt++;
                }
        if (cnt>hi)
        {
            hi=cnt;
            pmax=p;
        }
    }
    cout << "Number of solutions maximised when p=" << pmax << endl;
    return 0;
}
