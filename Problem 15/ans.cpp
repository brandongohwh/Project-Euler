#include<iostream>

using namespace std;

int main()
{
    long long int a[21][21];
    for(int b=0;b<21;b++)
    {
        a[b][0]=1;
        a[0][b]=1;
    }
    for(int b=1;b<21;b++)
        for(int c=1;c<21;c++)
            a[b][c]=a[b-1][c]+a[b][c-1];
    cout << "Number of routes: " << a[20][20] << endl;
    return 0;
}
