#include <iostream>
#include <format>
using namespace std;

int main() {
    double sum = 0.0;
    double k;
    cout<<"Enter the K >> "; cin>>k;
    for (int i = 1; i <= k; i++)
        sum += (2*i) + (k / (i + 3));
    cout<<"Sum is "<<sum<<endl;
}