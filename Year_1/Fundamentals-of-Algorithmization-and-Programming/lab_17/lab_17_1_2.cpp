#include <iostream>
using namespace std;

struct Price {
    int ruble;
    unsigned short coin;
};

struct Time {
    unsigned short hour;
    unsigned short minute;
    unsigned short second;
};

struct Date {
    unsigned short day;
    unsigned short month;
    int year;
};

struct Address {
    unsigned int index;
    char city[50];
    char street[50];
    unsigned short n_home;
    unsigned short flat;
};

struct Student {
    char first_name[50];
    char last_name[50];
    char middle_name[50];
    unsigned int n_RecordBook;
    unsigned short exam_grade;
};

struct Exam_report {
    char exam_name[50];
    char group_name[50];
    Date exam_date;
    Student students[30];
};

struct Complex {
    double re;
    double im;

    void input() {
        cout << "Re & Im >> ";
        cin >> re >> im;
    }

    void output() {
        cout << re << " + " << im << "i" << endl;
    }

    Complex add(Complex x) {
        Complex result;
        result.re = re + x.re;
        result.im = im + x.im;
        return result;
    }

};

int main() {
    Complex a;
    Complex b;


    a.input();
    a.output();
    b.input();
    b.output();

    Complex c = a.add(b);
    c.output();
    return 0;
}