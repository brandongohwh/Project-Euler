#include<iostream>

using namespace std;

int prime(long long int x)
{
    for (int a=2;a<x;a++)
        if (!(x%a))
            return 0;
    return 1;
}
int main()
{
    long long int a=1,cnt=0;
    while(cnt!=10001)
    {
        a++;
        if (prime(a))
            cnt++;
    }
    cout << "10001st prime number: "<< a <<endl;
    return 0;
}
