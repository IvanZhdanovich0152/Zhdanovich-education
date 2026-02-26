#include <iostream>
#include <iomanip>
#include <random>

using namespace std;

const int M = 10;
const int N = 9;

double fRand(double a, double b) {
    static random_device rd;
    static mt19937 gen(rd());
    uniform_real_distribution<> dis(a, b);
    return dis(gen);
}

void rand_arr(double** arr, int m, int n, double a, double b) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            arr[i][j] = fRand(a, b);
        }
    }
}

void show_arr(double** arr, int m, int n, double min_lim, double max_lim) {
    cout << endl << "Matrix " << " :" << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << '\t' << arr[i][j];
        }

        cout << endl;
    }


    cout << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] < min_lim + (max_lim - min_lim) / 2) {
                cout << '\t' << arr[i][j];

            }
            else {
                cout << '\t';
            }
        }
        cout << endl;
    }
    cout << endl;

    int counter[n]{0};

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[j][i] < min_lim + (max_lim - min_lim) / 2) {
                counter[i]++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (counter[i] <= 3) {
            cout << i+1 << " ";
        }
    }
    cout << endl;

}


int main() {
    int m, n;
    double a, b;

    double** matrix = new double*[M];
    for (int i = 0; i < M; i++)
        matrix[i] = new double[N];


    cout << fixed << setprecision(3);

    do {
        cout << "Enter 5 <= rows <= " << M << " -> ";
        cin >> m;
    } while (m < 5 || m > M);

    do {
        cout << "Enter 6 <= columns <= " << N << " -> ";
        cin >> n;
    } while (n < 6 || n > N);

    do {
        cout << "Enter a -> ";
        cin >> a;
        cout << "Enter b (b >= a) -> ";
        cin >> b;
    } while (a >= b);


    rand_arr(matrix, m, n, a, b);

    show_arr(matrix, m, n, a, b);


    for (int i = 0; i < M; i++)
        delete[] matrix[i];
    delete[] matrix;

    return 0;
}