#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 6; j++) {
            if (i > j) {cout << ".";}
            else if (j == 5) {cout << ".";}
            else if (i == 3) {cout << i; if (j == 6) cout<<"\n......";}
            else cout<<i;
        }
        cout<<endl;
    }
    return 0;
}


