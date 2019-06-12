#include<iostream>
#include<cmath>
#include<iomanip>

using namespace std;

int main()
{
    long long int sqs=0,ssq=0;
    for (int a=1;a<=100;a++)
    {
        sqs+=(a*a);
        ssq+=a;
    }
    ssq*=ssq;
    if (sqs>ssq)
        cout << "Difference between first hundred natural numbers: " << sqs-ssq << endl;
    else
        cout << "Difference between first hundred natural numbers: " << ssq-sqs << endl;
    return 0;
}
