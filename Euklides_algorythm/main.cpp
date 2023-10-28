#include <iostream>

using namespace std;

int gcd(int a, int b){

    while(b != 0){
        int mod = a%b;
        a = b;
        b = mod;
    }
    return a;
}

int main()
{
    int a;
    int b;
    cout<<"Input two integers, a and b (a > b): "<<endl;
    cin>>a;
    cin>>b;

    cout<<"The greatest common divisor: "<<gcd(a, b)<<endl;

    return 0;
}
