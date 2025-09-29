#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    float h = 0.25;
    for (float x = -4;  x <= 4; x += h) {
        for (float y = -4;  y <= 4; y += h) {
            //if (x == 0 or y == 0) cout << "0";
            if ((x>=0) and (y>=0)) cout << " ";
            else if ((abs(x)+abs(y)) <= 1) cout << " ";
            else if ((abs(x/2)+abs(y/2)) <= 1) cout << "#";
            else cout << " ";
        }
        cout << endl;
    }

    return 0;
}