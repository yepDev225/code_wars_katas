int digital_root(int n)
{
    int sum = 0;

    while (n > 9) {
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        n = sum;
        sum = 0;
    }

    return n;
}