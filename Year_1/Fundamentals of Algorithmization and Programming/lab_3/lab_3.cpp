#include <iostream>
using namespace std;

void func(int s ) {

}

int main() {
	setlocale(LC_ALL, "RU");

    int h, m, s;

    cin >> s;

    if (s < 60) {
		cout << s << " seconds" << endl;
	}
	else {
		m = s / 60;
		if (m < 60) {
			s = s % 60;
			cout << m << " minutes " << s << " seconds." <<endl;
		} else {
			h = m / 60;
			m %= 60;
			s %= 60;
			cout << h << " hours " << m << " minutes " << s << " seconds" << endl;
		}
		}

	return 0;
}
