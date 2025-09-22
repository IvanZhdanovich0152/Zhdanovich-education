#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

struct Point {
    double x;
    double y;
};

double calculateArea(Point a, Point b, Point c) {
    return abs((a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)) / 2.0);
}

int main() {

    Point p1, p2, p3;

    cout << "Enter:\n";
    cout << "Point 1 (x y): ";
    cin >> p1.x >> p1.y;

    cout << "Point 2 (x y): ";
    cin >> p2.x >> p2.y;

    cout << "point 3 (x y): ";
    cin >> p3.x >> p3.y;

    double area = calculateArea(p1, p2, p3);

    cout << fixed << setprecision(2);
    cout << "area : " << area << endl;

    return 0;
}
