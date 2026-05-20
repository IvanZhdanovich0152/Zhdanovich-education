#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

int count_letters(const string& str) {
    int count = 0;
    for (char c : str) //for (int i = 0; i < str.size(); i++) {str[i]}

        if (isalpha(c)) count++;
    return count;
}

int count_digits(const string& str) {
    int count = 0;
    for (char c : str)
        if (isdigit(c)) count++;
    return count;
}

bool hasOddcountletters(const string& str) {
    return count_letters(str) % 2 != 0;
}


int main() {
    ifstream fin("F1.txt");
    ofstream fout("Result.txt");

    if (!fin.is_open()) {
        cout << "Unable to open file F1.txt!" << endl;
        return 1;
    }
;
    string line;
    int totalLines = 0;
    int totalLetters = 0;
    int totalDigits = 0;

    while (getline(fin, line)) {
        if (!line.empty() &&
            isdigit(line[0]) &&
            hasOddcountletters(line)) {

            fout << line << endl;

            totalLines++;
            totalLetters += count_letters(line);
            totalDigits += count_digits(line);

        }
    }

    fout << "Lines: " << totalLines
         << ", Letters: " << totalLetters
         << ", Digits: "<< totalDigits << endl;

    fin.close();
    fout.close();

    cout << "Success!" << endl;
    return 0;
}