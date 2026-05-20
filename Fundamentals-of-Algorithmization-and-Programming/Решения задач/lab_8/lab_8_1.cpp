#include <iostream>
#include <cmath>
#include <iomanip>
#include <windows.h>
using namespace std;

// Функция для 5-го варианта
double f(double x) {
    return 1.3 * x + 1.4 * cos(x) - 0.6;
}

// Метод левых прямоугольников
double leftRect(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

// Метод правых прямоугольников
double rightRect(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

// Метод трапеций
double trapezoid(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = (f(a) + f(b)) / 2.0;
    for (int i = 1; i < n; i++) {
        sum += f(a + i * h);
    }
    return h * sum;
}

// Метод Симпсона
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

double F(double x) {
    return 0.65 * x * x + 1.4 * sin(x) - 0.6 * x;
}




// Точное значение интеграла
double exactIntegral(double a, double b) {
    // auto F = [](double x) { return 0.65 * x * x + 1.4 * sin(x) - 0.6 * x; }; //Первообразная
    // return F(b) - F(a);    // Формула Ньютона-Лейбница
    return F(b) - F(a);


}

int main() {
    SetConsoleOutputCP(CP_UTF8);

    double a = 0, b = M_PI / 3;
    int k;
    cout << "Введите k: ";
    cin >> k;

    cout << fixed << setprecision(4);

    cout << "n = " << k << ":\n";
    cout << "Левые прямоугольники: " << leftRect(a, b, k) << endl;
    cout << "Правые прямоугольники: " << rightRect(a, b, k) << endl;
    cout << "Трапеции: " << trapezoid(a, b, k) << endl;
    cout << "Симпсон: " << simpson(a, b, k) << endl;
    cout << "Точное значение: " << exactIntegral(a, b) << endl << endl;

    cout << "n = " << 10 * k << ":\n";
    cout << "Левые прямоугольники: " << leftRect(a, b, 10 * k) << endl;
    cout << "Правые прямоугольники: " << rightRect(a, b, 10 * k) << endl;
    cout << "Трапеции: " << trapezoid(a, b, 10 * k) << endl;
    cout << "Симпсон: " << simpson(a, b, 10 * k) << endl;
    cout << "Точное значение: " << exactIntegral(a, b) << endl;

    return 0;
}