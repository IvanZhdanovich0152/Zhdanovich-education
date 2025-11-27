#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

double fRand(double p){
    const double f = (double)rand() / RAND_MAX;
    return (0.5*p) + f * (3.5*p);
}

double avg_and_min(double arr[], int n) {
    double min = arr[0];
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        if (arr[i] <= min)
            min = arr[i];
    }
    for (int i = 0; i < n; i++) {
        if (arr[i] > min)
            sum += arr[i];
    }
    return sum/(n-1);
}

void rand_arr(double arr[], int n, double p) {
    for (int i = 0; i < n; i++) {
        arr[i] = fRand(p);
        cout << arr[i]<< " ";
    }
    cout <<endl<<"AVG >>> "<< avg_and_min(arr, n);
}

int main() {
    srand(time(0));
    cout << fixed << setprecision(3);

    const int n = 1 + rand() % 10;
    double arr[n];
    double p;

    cout<< "Enter p >= 2 >>> ";
    cin >> p;

    rand_arr(arr, n, p);

    return 0;
}