#include <iostream>
using namespace std;

// Разложение на произведение простых чисел и их показатель
// Prime Factorization

void factorize(unsigned int num) {
    // num -> prime factors

    int pre = 0;
    while (num % 2 == 0) {
        if (pre != 2) cout << "2 ";
        num = num / 2;
        pre = 2;
    }

    for (unsigned int i = 3; i * i <= num; i = i + 2) {
        while (num % i == 0) {
            if (pre != i) cout << i << " ";
            num = num / i;
            pre = i;
        }
    }

    if (num > 2) {
        if (pre != num) cout << num << " ";
        pre = num;
    }
}


int main() {
    /*
    Main function
    - Get user's number
    - Calculate result
    - Print result
    */

    cout << "-- Prime Factorization --" << endl;

    unsigned int num;
    bool rep = true;
    string cont;

    do {
        cout << "\nEnter the number to get it's prime factors: " << endl;
        cin >> num;
        cout << "The primer factors of " << num << " are:" << endl;
        factorize(num);
        cout << "\nContinue? (y,[n])" << endl;

        cin >> cont;
        if (cont != "y")
            rep = false;
    } while (rep);
    return 0;
}