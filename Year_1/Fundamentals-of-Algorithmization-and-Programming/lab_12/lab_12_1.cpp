#include <iostream>
#include <ctime>
using namespace std;


void rand_arr(int arr[], int m, int k) {
    for (int i = 0; i < m; i++) {
        arr[i] = k + rand() % (3*k);
        cout << arr[i]<< " ";
    }
}

int sum_even(int arr[], int m) {
    int sum = 0;
    for (int i = 0; i < m; i++) {
        if (arr[i] % 2 == 0) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    srand(time(0));
    const int m = 1 + rand() % 7;
    int array1[m];
    int array2[m];
    int array3[m];
    int array4[m];
    int k;
    cout<< "Enter 3 < k < 9 >>> ";
    cin >> k;

    cout<< "array1: "; rand_arr(array1, m, k);
    cout<<endl<< "array2: "; rand_arr(array3, m, k);
    cout<<endl<< "array3: "; rand_arr(array2, m, k);
    cout<<endl<< "array4: "; rand_arr(array4, m, k);

    int sum = sum_even(array1, m)+sum_even(array2, m)+sum_even(array3, m)+sum_even(array4, m);
    cout<<endl<<"Sum even:"<< sum;


    return 0;
}