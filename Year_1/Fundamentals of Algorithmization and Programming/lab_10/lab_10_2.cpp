#include <iostream>
using namespace std;



void flip(int* N) {
    int m = 0;
    while (*N) {
        m = m*10 + *N%10;
        *N = *N/10;
    }
    *N = m;
}

void flip(int& N) {
    int m = 0;
    while (N) {
        m = m*10 + N%10;
        N = N/10;
    }
    N = m;
}

int flip(int N) {
    int m = 0;
    while (N) {
        m = m*10 + N%10;
        N = N/10;
    }
    return m;

}

int main() {
    int N = 54321;
    flip(&N);
    cout << N << endl;
    flip(N);
    cout << N << endl;
    cout << flip(N) << endl;

    return 0;
}

