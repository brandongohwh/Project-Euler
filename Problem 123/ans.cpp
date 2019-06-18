#include<iostream>

using namespace std;

int prime(int x)
{
    int cnt=0;
    for(long long int a=2; a<=x; a++)
    {
        if (!(x%a))
            cnt++;
        if (cnt>1)
            return 0;
    }
    return 1;
}

int main()
{
    int x,cnt=0,pos,j;
    unsigned long long i=2,tot,pownum,minusnum,plusnum;
    while (1)
    {
        x=prime(i);
        if (x)
        {
            cnt++;
            minusnum=1;
            plusnum=1;
            for(j=0;j<cnt;j++)
            {
                minusnum*=(i-1);
                minusnum=(minusnum%(i*i));
                plusnum*=(i+1);
                plusnum=plusnum%(i*i);

            }
            tot=(plusnum+minusnum)%(i*i);
            if (tot > 10000000000)
            {
                pos=cnt;
                break;
            }
        }
        i++;
    }
    cout << "Least value of n where remainder exceeds 10^10: " << cnt << endl;
    return 0;
}
