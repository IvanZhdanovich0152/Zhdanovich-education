#include <iostream>
#include <format>
using namespace std;

int main() {
    int A;
    unsigned int i;

    cout << "Enter number A: ";
    cin >> A;

    cout << format("{:b}", A) << endl;

    cout << "Enter number i: ";
    cin >> i;
    A &= (~0 << i+1);

    cout << format("{:b} - {}", A, A) << endl;
    return 0;
}

