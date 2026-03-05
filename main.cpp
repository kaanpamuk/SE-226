#include <iostream>
using namespace std;
int main() {
    int x;
    int step=0;
    cout << "Enter a number: ";
    cin >> x;
    while (x!=1) {
        if (x%2==0) {
            x=x/2;
        }
        else {
            x=x*3+1;
        }
        cout << "--> " << x;
        step++;
    }
    cout << endl;
    cout <<"Total step is : " << step << endl;



    return 0;
}