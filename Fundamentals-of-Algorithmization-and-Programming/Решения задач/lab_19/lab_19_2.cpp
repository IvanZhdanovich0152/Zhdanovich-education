#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <ctime>
using namespace std;



string createFileOut();
void fill_file(string fileName);

short randShort(int min, int max);
float randFloat(float min, float max);

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));
    string currentPath = createFileOut();
    fill_file(currentPath);
    return 0;
}

string createFileOut() {
    string path;
    cout << "Введите имя файла (без .txt)>>> "; cin >> path;

    return path;
}

short randShort(int min, int max) {
    short res = min + rand() % (max - min + 1);
    return res;
}

float randFloat(float min, float max) {
    float res = min + static_cast<float>(rand()) / RAND_MAX * (max - min);
    return res;
}

void fill_file(string fileName) {
    short m = randShort(4, 12);
    short k;
    float a, b;

    cout << "Введите a >>> "; cin >> a;
    cout << "Введите b >>> "; cin >> b;

    ofstream fout(fileName + ".txt");
    fout << m <<endl;
    for (int i = 1; i <= m; i++) {
        k = randShort(5, 11);
        fout << k << " ";
        float sum = 0;
        for (int j = 1; j <= k; j++) {
            if (j == 1 || j == k) {
                float num = randFloat(a, b);
                sum += num;
                fout << num << " ";
            }
            else
                fout << randFloat(a, b) << " ";
        }
        cout << "Ряд "<< i <<" | Сумма: " << sum << endl;
        fout << endl;
    }
    fout.close();
}
