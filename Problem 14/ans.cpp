#include<iostream>

using namespace std;

int main()
{
    long int a,maxint;
    long long int x;
    int b,hi=0;

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
        if (hi<b)
        {
            hi=b;
            maxint=a;
        }
    }
    cout << "Starting number " << maxint << " produces the longest chain of length " << hi << endl;
    return 0;
}
