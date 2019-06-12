#include<iostream>

using namespace std;

int prime(long long int x)
{
    for(int a=2;a<x;a++)
        if (!(x%a))
            return 0;
    return 1;
}

int main()
{
    long long int sum=0,a;
    for (a=2;a<2000000;a++)
        if (prime(a))
               sum+=a;
    cout << "Sum of primes <20000000: " << sum << endl;
    return 0;
}
