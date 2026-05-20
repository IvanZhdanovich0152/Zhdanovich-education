#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");

    char ans;

    cout << "Enter the char: A S D F B R >>> "; cin >> ans;

    switch (ans) {
        case 'A': cout << "Access" << endl;
            break;
        case 'B': cout << "Browse" << endl;
            break;
        case 'D': cout << "Desktop" << endl;
            break;
        case 'F': cout << "Favor" << endl;
            break;
        case 'R': cout << "Reverse" << endl;
            break;
        case 'S': cout << "Sales" << endl;
            break;
        default:
            cout << "Invalid Input" << endl;
    }

    return 0;
}
