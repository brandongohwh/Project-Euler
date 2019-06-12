#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    long int sum=0,x1=1,x2=2,x3=3;

    while(x1<=4*pow(10,6))
    {
        if (!(x1%2))
            sum+=x1;
        x1=x2;
        x2=x3;
        x3=x1+x2;
    }
    cout << "Sum of even numbered Fibonacci numbers <= 4 million: "<< sum << endl;
    return 0;
}
