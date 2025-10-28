#include <iostream>
#include <cmath>
#include <iomanip>
#include <windows.h>
using namespace std;

double f(double x) {
    return 1.3 * x + 1.4 * cos(x) - 0.6;
}

double leftRect(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

double rightRect(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

double trapezoid(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = (f(a) + f(b)) / 2.0;
    for (int i = 1; i < n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

double simpson(double a, double b, int n) {
    if (n % 2 != 0) n++;
    double h = (b - a) / n;
    double sum = f(a) + f(b);
    for (int i = 1; i < n; i += 2) {
        sum += 4 * f(a + i * h);
    }
    for (int i = 2; i < n; i += 2) {
        sum += 2 * f(a + i * h);
    }
    return h * sum / 3.0;
}

double integrate(double a, double b) {
    cout << "Через формулу Ньютона-Лейбница: ";
    auto F = [](double x) { return 0.65 * x * x + 1.4 * sin(x) - 0.6 * x; };
    return F(b) - F(a);
}

double integrate(double a, double b, int n, const string& method) {
    if (method == "l") {
        cout << "Метод левых прямоугольников: ";
        return leftRect(a, b, n);
    } else if (method == "r") {
        cout << "Метод правых прямоугольников: ";
        return rightRect(a, b, n);
    } else if (method == "tr") {
        cout << "Метод трапеций: ";
        return trapezoid(a, b, n);
    } else if (method == "simp") {
        cout << "Метод Симпсона: ";
        return simpson(a, b, n);
    } else {return integrate(a, b);}

}


int main() {
    SetConsoleOutputCP(CP_UTF8);

    double a = 0, b = M_PI / 3;
    int k;
    cout << "Введите k: ";
    cin >> k;

    cout << fixed << setprecision(4);

    cout << "n = " << k << ":\n";
    cout << integrate(a,b,k,"l") << endl;
    cout << integrate(a,b,k,"r") << endl;
    cout << integrate(a,b,k,"tr") << endl;
    cout << integrate(a,b,k,"simp") << endl;
    cout << integrate(a, b) << endl << endl;

    cout << "n = " << 10 * k << ":\n";
    cout << integrate(a,b,k*10,"l") << endl;
    cout << integrate(a,b,k*10,"r") << endl;
    cout << integrate(a,b,k*10,"tr") << endl;
    cout << integrate(a,b,k*10,"simp") << endl;
    cout << integrate(a, b) << endl << endl;

    return 0;
}