#include <iostream>
#include <windows.h>
using namespace std;

int f(int N) {
    int m = 0;
    while (N) {
        m = m*10 + N%10;
        N = N/10;
    }
    return m;
}

void flip(int* N) {
    *N = f(*N);
}

void flip(int& N) {
    N = f(N);
}

int flip(int N, bool is_true) {
    return f(N);
}

int main() {
    SetConsoleOutputCP(CP_UTF8);
    bool is_true = true;
    int N = 54321;
    cout << N << endl;
    flip(&N);
    cout << "Flip с указателем >>> " << N << endl;
    flip(N);
    cout << "Flip с ссылкой >>> " << N << endl;
    cout << "Flip значения >>> " << flip(N, is_true) << endl;


    cout<< f(1234)<<endl;

    return 0;
}

