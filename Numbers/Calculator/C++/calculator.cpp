#include <iostream>
#include <string>   
#include <math.h>   

using namespace std;

// Калькулятор
// Calculator

std::string toString(int arg)
{
    return std::to_string(arg);
}

string calculator(int num1, int num2, char op) {

    string a = toString(num1) + " ";
    string b = toString(num2) + " = ";

    string symbols = "+-/*^";
    if (symbols.find(op) != std::string::npos) {
        switch (op) {
        case '+':
            return a + op + ' ' + b + toString(num1 + num2);
        case '-':
            return a + op + ' ' + b + toString(num1 - num2);
        case '*':
            return a + op + ' ' + b + toString(num1 * num2);
        case '/':
            return a + op + ' ' + b + toString(num1 / num2);
        case '^':
            return a + op + ' ' + b + toString(pow(num1, num2));

        }
    }
    else
        cout << "Please only type one of these characters: +, -, *, /!";


}


int main() {
    /*
    Main function
    - Get user's number
    - Calculate result
    - Print result
    */

    cout << "-- Calculator --" << endl;

    unsigned int num1,num2;
    char op;
    bool rep = true;
    string cont;

    do {
        cout << "\nType the first number: " << endl;
        cin >> num1;
        cout << "\nType the second number: " << endl;
        cin >> num2;
        cout << "What kind of operation would you like to do? \nChoose between + , -, *, / , ^ : " << endl;
        cin >> op;
        cout << calculator(num1, num2, op);
        cout << "\nContinue? (y,[n])" << endl;

        cin >> cont;
        if (cont != "y")
            rep = false;
    } while (rep);

    return 0;
}


