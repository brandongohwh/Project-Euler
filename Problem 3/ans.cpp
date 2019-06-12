#include<iostream>

using namespace std;

int prime(long long int x);

int main()
{
    long long int div=2,max=0,cur,num=600851475143;
    int a;
    cur=num;
    while(cur!=1)
    {
        if (!(cur%div))
        {
            if (prime(div))
                if (div>max)
                    max=div;
            cur/=div;
            div=2;
            continue;
        }
        div++;
    }
    cout << "Largest prime factor of " << num << " is: " << max << endl;
    return 0;
}

int prime(long long int x)
{
    for(long int a=2;a<x;a++)
        if (!(x%a))
            return 0;
    return 1;
}
