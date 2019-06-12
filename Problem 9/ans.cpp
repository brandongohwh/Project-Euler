#include<iostream>

using namespace std;

int main()
{
    for(int c=0; c<=1000; c++)
        for(int b=0; b<c; b++)
            for(int a=0; a<b; a++)
                if (a+b+c==1000 && c*c==a*a+b*b)
                    cout << "Product: " << a*b*c << ", a: " << a << ", b: " << b << ", c: " << c << endl;
    return 0;
}
