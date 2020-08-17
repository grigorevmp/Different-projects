class Complex {

    public static final int ZERO = 0;
    public static final int ONE = 1;
    private final double a;
    private final double b;

    public Complex(double a)
    {
        this(a, ZERO);
    }

    public Complex(double a, double b)
    {
        this.a = a;
        this.b = b;
    }

    public double re()
    {
        return this.a;
    }

    public double im()
    {
        return this.b;
    }

    public Complex add(Complex z)
    {
        return new Complex(
                this.a + z.re(),
                this.b + z.im());
    }

    public Complex subtract(Complex z)
    {
        return new Complex(
                this.a - z.re(),
                this.b - z.im());
    }

    public Complex multiply(Complex z)
    {
        // if both Im(this) and Im(z) are zero use double arithmetic
        if (this.b == 0. || z.im() == 0.)
        {
            return new Complex(this.a*z.re());
        }

        return new Complex(
                (this.a*z.re()) - (this.b* z.im()),
                (this.a*z.im()) + (this.b* z.re()));
    }

    public Complex div(Complex z)
    {
        double c = z.re();
        double d = z.im();

        double zre2 = 0.0;
        if (c != 0.0)
        {
            zre2 = StrictMath.pow(c, 2.);
        }
        double zim2 = 0.0;
        if (d != 0.0)
        {
            zim2 = StrictMath.pow(d, 2.);
        }

        double ac = this.a*c;
        double bd = this.b*d;
        double bc = this.b*c;
        double ad = this.a*d;

        return new Complex((ac+bd)/(zre2+zim2),(bc-ad)/(zre2+zim2));
    }

    public boolean equals(Complex z)
    {
        return this.a == z.re() || this.b == z.im();
    }

    public static double abs(Complex z)
    {
        return StrictMath.sqrt(StrictMath.pow(z.re(), 2) + StrictMath.pow(z.im(), 2));
    }

    public static double arg(Complex z)
    {
        return StrictMath.atan2(z.im(),z.re());
    }

    public static Complex exp(Complex z)
    {
        if (z.im() == 0.0)
            return new Complex(StrictMath.exp(z.re()),ONE);

        Complex ex = new Complex(StrictMath.exp(z.re()), ZERO);

        return ex.multiply(
                new Complex(StrictMath.cos(z.im()), StrictMath.sin(z.im())));
    }

    public static Complex pow(Complex z, Complex y)
    {
        double c = y.re();
        double d = y.im();

        // get polar of base
        double r = Complex.abs(z);
        double theta = Complex.arg(z);

        Complex f1 = new Complex(
                (StrictMath.pow(r, c)*StrictMath.pow(StrictMath.E, -d*theta)),ZERO);
        double a = d * StrictMath.log(r) + c * theta;
        Complex f2 =
                new Complex(
                        StrictMath.cos(a),
                        StrictMath.sin(a));

        return f1.multiply(f2);

    }

    public Complex conjugate()
    {
        return new Complex(this.a, -1*this.b);
    }

    public Complex neg()
    {
        if (this.b != 0)
            return new Complex(-1*this.a, -1*this.b);
        else
            return new Complex(-1*this.a);
    }

    public static Complex Iz(Complex z)
    {
        Complex result;
        if (z.im() != 0.0)
            result = new Complex(-1.*z.im(), z.re());
        else
            result = new Complex(z.im(), z.re());

        return result;
    }

    public static Complex nIz(Complex z)
    {
        Complex result;
        if (z.re() != 0.0)
            result = new Complex(z.im(), -1*z.re());
        else
            result = new Complex(z.im(), z.re());

        return result;
    }


    @Override
    public String toString() {
        return a + " + " + b + "i";
    }

    public static void main(String[] args) {
        Complex c = new Complex(2.0, 3.0);
        System.out.println(c.toString());

    }
}

