#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");

    char ans;

    cout << "Enter the char: M S N L B >>>"; cin >> ans;

    switch (ans) {
        case 'M': cout << "Minsk" << endl;
            break;
        case 'B': cout << "Brest" << endl;
            break;
        case 'L': cout << "Lida" << endl;
            break;
        case 'N': cout << "Novopolotsk" << endl;
            break;
        case 'S': cout << "Slonim" << endl;
            break;
        default:
            cout << "Invalid Input" << endl;
    }


    return 0;
}
