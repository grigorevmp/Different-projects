#include <iostream>
#include <string>   
#include <math.h>   

using namespace std;

// Factorial

static string const TOOGLE = "cycle";  // recursion

int recur_factorial(int num) {
    if (num == 1)
        return num;
    else
        return num * recur_factorial(num - 1);
}

int fact(int num) {
    //  N -> factorial

    int result = 1;

    if (TOOGLE == "cycle") 
        for (int i = 0; i < num; ++i)
            result *= (i + 1);
    
    if (TOOGLE == "recursion") 
        result = recur_factorial(num);
    

    return result;

}


int main() {
    /*
    Main function
    - Get user's number
    - Calculate result
    - Print result
    */

    cout << "-- Calculator --" << endl;

    unsigned int num;
    bool rep = true;
    string cont;

    do {
        cout << "\nInput number: " << endl;
        cin >> num;

        cout << endl << fact(num) << endl;
        cout << "\nContinue? (y,[n])" << endl;

        cin >> cont;
        if (cont != "y")
            rep = false;
    } while (rep);

    return 0;
}


