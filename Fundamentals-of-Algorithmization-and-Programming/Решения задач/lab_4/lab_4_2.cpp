#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "RU");
    float h = 0.125   ;
    for (float y = -4;  y <= 7; y += h) {
         for (float x = -4;  x <= 9; x += h){
            //if (x == 0 or y == 0) cout << "0";

            if ((x <= 6) and (x >= 4) and (y == 0) ) cout << "-";

            else if ((y <= 6) and (y >= 4) and (x == 0) ) cout << "|";

            else if ((x*x + y*y < 36) and (x*x + y*y > 16) and (x >= 0) and (y >= 0)) cout << '.';

            else if (x*x + y*y > 4) cout << '#';

            else if (x*x + y*y == 4) cout << '/';

            else cout << '.';

        }
        cout << endl;
    }

    return 0;
}