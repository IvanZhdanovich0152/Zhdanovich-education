#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    float h = 0.1   ;
    for (float x = -2;  x <= 6; x += h) {
        for (float y = -2;  y <= 6; y += h) {
            //if (x == 0 or y == 0) cout << "0";

            if ((x <= 6) and (x >= 4) and (y == 0) ) cout << "|";

            else if ((y <= 6) and (y >= 4) and (x == 0) ) cout << "-";

            else if ((x*x + y*y < 36) and (x*x + y*y > 16) and (x >= 0) and (y >= 0)) cout << ' ';

            else if (x*x + y*y > 4) cout << '#';

            else if (x*x + y*y == 4) cout << '/';

            else cout << ' ';

        }
        cout << endl;
    }

    return 0;
}