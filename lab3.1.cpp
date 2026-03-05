#include <iostream>
using namespace std;
int main() {
    int x=0;
    cout<<"Enter a number between 10 and 100 ";
    cin>>x;
    while(x < 10 or x > 100) {
        cout<<"Enter a number between 10 and 100 ";
        cin>>x;
    }
    int fizz=0;
    int buzz=0;
    int fizzbuzz=0;

    for(int i=1;i<=x;i++) {
        if (i%7==0) {
            continue;
        }
        if (i%3==0 && i%5==0) {
            cout<<"Fizzbuzz"<<endl;
            fizzbuzz++;
        }
        if (i%3==0) {
            cout<<"fizz"<<endl;
            fizz++;
        }
        if (i%5==0) {
            cout<<"buzz"<<endl;
            buzz++;
        }
        else {
            cout<<i<<endl;
        }
        cout << "Summary:\n" << endl;
        cout << "Fizz count: " << fizz << endl;
        cout << "Buzz count: " << buzz << endl;
        cout << "FizzBuzz count: " << fizzbuzz << endl;
    }

    return 0;
}