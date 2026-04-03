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

    cout << ((A >> i) & 1 )<< endl;
    return 0;
}


