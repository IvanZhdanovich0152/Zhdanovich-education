#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double f(double x) {
    return x*x*x*x*x - 8.3*x - 4;
}

int main() {
    cout << fixed << setprecision(5);
    double lim[2];
    cout<<"Enter a, b >>> ";
    cin>>lim[0]>>lim[1];

    if (f(lim[0]) * f(lim[1]) >= 0) {
        cout<<"Error: f(a) and f(b) must have opposite signs!"<<endl;
        return 1;
    }

    const double tolerance = 0.001;
    const int max_iteration = 100;
    double x_mid;
    int iteration = 0;

    do {
        x_mid = lim[0] + (lim[1]-lim[0])/2.0;
        if (f(x_mid)==0.0) {
            break;
        }
        else if ( f(lim[0]) * f(x_mid) <0) {
            lim[1] = x_mid;
        }
        else {
            lim[0] = x_mid;
        }
        iteration++;

    } while (fabs(lim[1] - lim[0]) > tolerance && iteration < max_iteration);

    x_mid = lim[0] + (lim[1]-lim[0])/2.0;

    cout << "Root: " << x_mid << endl;
    cout << "f(root) = " << f(x_mid) << endl;
    cout << "Iterations: " << iteration << endl;
    cout << "Final interval: [" << lim[0] << ", " << lim[1] << "]"<< endl;
    return 0;
}