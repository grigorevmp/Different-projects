#include <iostream>
using namespace std;

// Введите число, и программа сгенерирует N членов последовательности Фибоначчи.
// Enter a number and the program will generate N members a Fibonacci series.


void fibonacci(unsigned int N) {
    //  N -> fibonacci series

    long t1 = 0, t2 = 1, nextTerm = 0;

   for (int i = 1; i <= N; ++i)
   {
       if (i == 1)
       {
           cout << t1 << " ";
           continue;
       }
       if (i == 2)
       {
           cout << t2 << " ";
           continue;
       }
       nextTerm = t1 + t2;
       t1 = t2;
       t2 = nextTerm;

       cout << nextTerm << " ";
   }
}


int main() {
    /*
    Main function
    - Get user's number
    - Calculate result
    - Print result
    */

    cout << "-- Fibonacci series --" << endl;

    unsigned int num;
    bool rep = true;
    string cont;

    do {
        cout << "\nEnter the number of Fibonacci sequence members you want to see: " << endl;
        cin >> num;
        fibonacci(num);
        cout << "\nContinue? (y,[n])" << endl;

        cin >> cont;
        if (cont != "y")
            rep = false;
    } while (rep);

    return 0;
}


