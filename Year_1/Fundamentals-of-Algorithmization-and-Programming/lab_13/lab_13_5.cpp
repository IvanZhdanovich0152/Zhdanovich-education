#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr_str[12];
    string right_arr_str[12];
    int count_char = 0;
    int k = 0;
    for (auto & str : arr_str) { //range-based for
        cout << "Enter string ->";
        cin >> str;
    }

    for (auto & str : arr_str) {
        count_char = 0;
        for (int j = 0; j < 50; j++) {
            if (str[j] == '+' || str[j] == '*' || str[j] == '%') {
                count_char++;
                if (count_char == 3) {
                    right_arr_str[k] = str;
                    k++;
                    break;
                }
            }
        }
    }
    for (const auto & elem : right_arr_str) {
        cout << elem << endl;
    }



    return 0;
}