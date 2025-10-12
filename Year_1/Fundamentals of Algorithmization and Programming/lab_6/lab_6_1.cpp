#include <math.h>
#include <iostream>
using namespace std;

int main() {
    float x0, x1, dx;

    cout<<"Enter the value of x0: "; cin>>x0;
    cout<<"Enter the value of x1: "; cin>>x1;
    cout<<"Enter the value of dx: "; cin>>dx;

    while (x0 <= x1) {
        double f_x = -2.4*x0*x0+1/(x0+0.5)-sin(x0*x0);
        cout << x0 << " | " << f_x << endl;
        x0 += dx;
    }
    return 0;
}