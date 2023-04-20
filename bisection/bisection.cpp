#include <iostream>
#include <cmath>

using namespace std;

float a=10;
float b=sqrt(a);
float x=0;
float y=5;
float z;
float z_2=z*z;
float e=0.01;

float fun_z(){
    z=(x+y)/2;
    return z;
}

int main()
{
    while (abs(a-z_2)>=e)
    {
        if (z_2>a)
        {
            y=z;
            fun_z();
        }
        else
        {
            x=z;
            fun_z();
        }
        z_2=z*z;
    }
    cout<<"Liczba a="<<a<<endl;
    cout<<"Pierwiastek z a (funkcja sqrt()) b="<<b<<endl;
    cout<<"Pierwiastek z a (metoda bisekcji), dla e="<<e<<", z="<<z<<endl;

}
