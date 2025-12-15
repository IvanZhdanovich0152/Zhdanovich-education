#include <iostream>
#include <iomanip>
#include <random>

using namespace std;

const int M = 5;
const int N = 6;

double fRand(double p) {
    static random_device rd;
    static mt19937 gen(rd());
    uniform_real_distribution<> dis(-p, 2 * p);
    return dis(gen);
}

void rand_arr(double arr[M][N], int m, int n, double k) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            arr[i][j] = fRand(k);
        }
    }
}

void show_arr(double arr[M][N], int m, int n, string name) {
    cout << endl << "Matrix " << name << " :" << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << '\t' << arr[i][j];
        }
        cout << endl;
    }
}


int main() {
    int m, n;
    double k;
    double matrix_A[M][N];
    double matrix_B[M][N];
    double matrix_C[M][N];

    cout << fixed << setprecision(3);

    do {
        cout << "Enter 2 <= columns <= " << M << " -> ";
        cin >> m;
    } while (m < 2 || m > M);

    do {
        cout << "Enter 2 <= rows <= " << N << " -> ";
        cin >> n;
    } while (n < 2 || n > N);

    do {
        cout << "Enter 1.5 <= k <= 4.5 -> ";
        cin >> k;
    } while (k < 1.5 || k > 4.5);

    rand_arr(matrix_A, m, n, k);
    rand_arr(matrix_B, m, n, k);
    rand_arr(matrix_C, m, n, k);

    show_arr(matrix_A, m, n, "A");
    show_arr(matrix_B, m, n, "B");
    show_arr(matrix_C, m, n, "C");



    return 0;
}