#include <math.h>
#include <iostream>
using namespace std;

int main() {
    float x, sum = 0;
    int n = 0;

    cout<<"Enter the value of x: "; cin>>x;
    double f_x = 2.1-sin(x*x-1);

    do {
        n++;
        sum += 1.0/n;
    } while (sum <= f_x);

    cout << f_x << endl;
    cout << sum << endl;
    cout << n << endl;

    return 0;
}