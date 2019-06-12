#include <iostream>

using namespace std;

int main()
{
    int sum=0;
    for(int a=0;a<1000;a++)
        if ((!(a%3))||(!(a%5)))
            sum+=a;
    cout << "Sum of multiples of 3 OR 5 below 1000: " << sum << endl;
    return 0;
}
