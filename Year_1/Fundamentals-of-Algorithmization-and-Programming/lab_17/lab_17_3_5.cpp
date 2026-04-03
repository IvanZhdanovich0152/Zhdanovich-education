#include <iostream>
#include <string>
using namespace std;

struct Student {
    char first_name[50];
    char last_name[50];
    char middle_name[50];
    string gender;
    unsigned short age;
    unsigned short year;
    float performance;

    void input() {
        cout<<"Enter the first name: "; cin >> first_name;
        cout<<"Enter the last name: "; cin >> last_name;
        cout<<"Enter the middle name: "; cin >> middle_name;
        cout<<"Enter the gender: "; cin >> gender;
        cout<<"Enter the age: "; cin >> age;
        cout<<"Enter the year: "; cin >> year;
        cout<<"Enter the performance: "; cin >> performance;
        cout<<endl;
    }

    void output() {
        cout << "Student " << first_name << " " << last_name << " " << middle_name << endl;
        cout << "Gender: " << gender << endl;
        cout << "Age: " << age << endl;
        cout << "Year: " << year << endl;
        cout << "Performance: " << performance << endl;
        cout << endl;
    }
};

void fill_arr(Student *students, int m) {
    for (int i = 0; i < m; i++)
        students[i].input();
}

void print_arr(Student *students, int m) {
    for (int i = 0; i < m; i++)
        students[i].output();
}

int counter_male(Student *students, int m, int n) {
    int counter = 0;
    for (int i = 0; i < m; i++)
        if (students[i].gender == "male" && students[i].year == n) {
            counter++;
        }
    return counter;
}

int main() {
    int m;
    int n = 1;
    cout<<"Enter the number of students: "; cin >> m;
    Student *students = new Student[m];

    fill_arr(students, m);
    print_arr(students, m);
    cout<< counter_male(students, m, n);

    delete[] students;
    students = nullptr;
    return 0;
}

