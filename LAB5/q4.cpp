#include <iostream>
using namespace std;



double func(int n) {
    if (n==1)
        return 1.0;
    double step;
    if (n % 2 == 0)
        step= -1.0/ n;
    else
        step=1.0 /n;

    return func(n - 1) + step;
}


int main() {


    int n;
    cout << "enter number: ";
    cin >> n;

    double result = func(n);
    cout << "result: " << result << endl;
    return 0;
}