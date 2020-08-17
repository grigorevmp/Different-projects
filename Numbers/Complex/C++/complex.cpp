#include <iostream> 

class Complex
{
private:
    double a, b;
public:

    Complex() { 
        a = 0; 
        b = 0; 
    }

    Complex(double r, double i) {
        a = r;
        b = i; 
    }

    Complex(const Complex& ob) {
        a = ob.a;
        b = ob.b; 
    };

    Complex& operator = (Complex);
    Complex operator + (Complex);
    Complex operator - (Complex);
    Complex operator * (Complex&);
    Complex operator / (Complex&);
    Complex& operator += (Complex);
    Complex& operator -= (Complex);
    Complex& operator *= (Complex);
    Complex& operator /=(Complex);
    friend std::istream& operator >>(std::istream&, Complex&);
    friend std::ostream& operator << (std::ostream&, const Complex&);
    bool operator == (Complex& z);
    bool operator != (Complex& z);
    bool operator > (Complex& z);
    bool operator < (Complex& z);

};

bool Complex:: operator > (Complex& z)
{
    if (this->a > z.a)
        return 1;
    else if (this->a == z.a && this->b > z.b)
        return 1;
    else
        return 0;
}

bool Complex ::operator < (Complex& z)
{
    if (this->a < z.a)
        return 1;
    else if (this->a == z.a && this->b < z.b)
        return 1;
    else
        return 0;

}

bool Complex::operator != (Complex& z)
{
    if (this->a != z.a || this->b != z.b)
        return 1;
    else
        return 0;
}

bool Complex::operator==(Complex& z)
{
    if (this->a == z.a && this->b == z.b)
        return 1;
    else
        return 0;
}

Complex Complex::operator*(Complex& z)
{
    double i, j;
    i = a * z.a - b * z.b;
    j = a * z.b + z.a * b;
    a = i;
    b = j;
    return *this;
}

Complex Complex::operator/(Complex& z)
{
    double i, j, k;
    k = a * a + z.b * z.b;
    i = (a * z.a + b * z.b) / k;
    j = (z.a * b - a * z.b) / k;
    a = i;
    b = j;
    return *this;
}

Complex& Complex::operator =(Complex z)
{
    this->a = z.a;
    this->b = z.b;
    return *this;
}

Complex Complex::operator+(Complex z)
{
    this->a = this->a + z.a;
    this->b = this->b + z.b;
    return *this;
}

Complex Complex::operator-(Complex z)
{
    this->a = this->a - z.a;
    this->b = this->b - z.b;
    return *this;
}


std::ostream& operator << (std::ostream& out, const Complex& z)
{
    if (z.b < 0)
        out << z.a << "+i(" << z.b << ")\n";
    else
        out << z.a << "+i" << z.b << "\n";
    return out;
}

std::istream& operator >> (std::istream& in, Complex& z)
{
    std::cout << "Input real part: ";
    in >> z.a;
    std::cout << "Input imagine part: ";
    in >> z.b;
    return in;
}

Complex& Complex::operator+=(Complex z)
{
    a += z.a;
    b += z.b;
    return *this;
}

Complex& Complex::operator-=(Complex z)
{
    a -= z.a;
    b -= z.b;
    return *this;
}

Complex& Complex::operator*=(Complex z)
{
    a *= z.a;
    b *= z.b;
    return *this;
}

Complex& Complex::operator/=(Complex z)
{
    a /= z.a;
    b /= z.b;
    return *this;
}

int main()
{
    setlocale(0, "rus");
    Complex z;
    std::cin >> z;
    std::cout << z << std::endl;
}