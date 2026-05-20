#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

struct PRICE {
private:
    int id;
    string title_product;
    string name_shop;
    double price;
    int count_product_in_storage;

public:
    PRICE () {
        id = 0;
        title_product = "";
        name_shop = "";
        price = 0.0;
        count_product_in_storage = 0;
    }
    ~PRICE() {}

    void input();
    void print() const;

    int get_id() const { return id; }
    string get_title_product() const { return title_product; }
    string get_name_shop() const { return name_shop; }
    double get_price() const { return price; }
    int get_count_product_in_storage() const { return count_product_in_storage; }


    void edit();
};

void PRICE::input() {
    cout<<"Enter the id: "; cin >> id;
    cout<<"Enter the title_stuff: "; cin >> title_product;
    cout<<"Enter the name_shop: "; cin >> name_shop;
    cout<<"Enter the price: "; cin >> price;
    cout<<"Enter the count_stuff: "; cin >> count_product_in_storage;
    cout<<endl;
}

void PRICE::print() const{
    cout << "ID: " << id << endl;
    cout << "Title product '" << title_product << "' "<< endl;
    cout << "Shop '" << name_shop << "' "<< endl;
    cout << "Price: " << price << "p"<< endl;
    cout << "Count at store: " << count_product_in_storage << endl;
    cout << endl;
}

void PRICE::edit() {
    cout << "Editing product ID " << id << endl;
    cout << "New title: "; cin >> ws; getline(cin, title_product);
    cout << "New shop: "; getline(cin, name_shop);
    cout << "New price: "; cin >> price;
    cout << "New count: "; cin >> count_product_in_storage;
}

PRICE* inputArray(int& n) {
    PRICE* arr = new PRICE[n];
    for (int i = 0; i < n; i++) {
        cout << "Product #" << i+1 <<endl;
        arr[i].input();
    }
    return arr;
}

void printArray(const PRICE* arr, const int n) {
    if (n == 0) {
        cout << "Array is empty.\n";
        return;
    }
    cout << "\n--- Product List ---\n";
    for (int i = 0; i < n; i++)
        arr[i].print();
}

int main() {
    int count_elem = 0;
    int choice;
    PRICE* products = nullptr;

    do {
        cout << "1 - InputArray\n2 - PrintArray\n0 - Exit" << endl;
        cout <<">>> "; cin >> choice;
        switch (choice) {
            case 1:
                delete[] products;
                cout<<"Enter the number of products: "; cin >> count_elem;
                products = inputArray(count_elem);
                break;
            case 2:
                printArray(products, count_elem);
                break;
            case 0:
                cout << "Exiting...\n"<<endl;
                break;
            default:
                cout << "Wrong choice.\n";
        }
    } while (choice != 0);


    delete[] products;
    return 0;
}