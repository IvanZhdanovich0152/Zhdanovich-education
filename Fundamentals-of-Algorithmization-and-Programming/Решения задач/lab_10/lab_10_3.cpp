#include <iostream>
using namespace std;

void f(int N, int& First, int& Last) {
    while (N) {
        int temp = 0;
        temp = temp*10+N%10;
        if (temp > First) {
            First = temp;
        }
        if (temp < Last) {
            Last = temp;
        }
        N = N / 10;
    }

}

int main() {
    int N, First=-1,Last=10;
    cout << "Enter the number: "; cin >> N;

    f(N,First,Last);
    cout << First << ' ' << Last << endl;
    return 0;
}