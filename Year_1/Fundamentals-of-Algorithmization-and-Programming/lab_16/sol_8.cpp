#include <iostream>
#include <format>
using namespace std;

int main() {
    int A;
    int i;
    cin >> A;
    cout << format("{:b}", A) << endl;
    cin >> i;

    cout << (A & (1 << i) >> i) << endl;
}

