#include <iostream>
using namespace std;

short graph_2(float x, float y) {
    if (x == 0 or y == 0)
        return 0;
    else if ((x*x + y*y < 36) and (x*x + y*y > 16) and (x >= 0) and (y <= 0))
        return 1;
    else if (x*x + y*y < 4)
        return 1;
//    else if (x*x + y*y == 4) return 2;
    else
        return -1;
}
 short graph_5(float x, float y) {
    if (x == 0 or y == 0) return 0;
    else if ((x>=0) and (y<=0)) return 1;
    else if ((abs(x)+abs(y)) <= 1) return 1;
    else if ((abs(x/2)+abs(y/2)) <= 1) return -1;
    else return 1;
}


int main() {
    float x_min = -10.0;
    float y_min = 7.0;
    float x_max = 10.0;
    float y_max = -10.0;

    float dh = 0.25;
    short ans;

    cout << "Enter number graf >>>  "; cin >> ans; cout << endl;

    if (ans == 2)
    {
        for (float y = y_min;  y >= y_max; y -= dh) {
            for (float x = x_min;  x <= x_max; x += dh) {
                short result = graph_2(x, y);
                switch (result) {
                    case -1: cout << "X"; break;
                    case 0: cout << "*"; break;
                    case 1: cout << " "; break;
                }
            }
            cout << endl;
        }
    }
    else if (ans == 5)
    {
        for (float y = y_min;  y >= y_max; y -= dh) {
            for (float x = x_min;  x <= x_max; x += dh) {
                short result = graph_5(x, y);
                switch (result) {
                    case -1: cout << "X"; break;
                    case 0: cout << "*"; break;
                    case 1: cout << " "; break;
                }
            }
            cout << endl;
        }
    }


    return 0;
}