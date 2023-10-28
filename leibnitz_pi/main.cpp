#include <iostream>
#include <iomanip>
#include <cmath>


using namespace std;

double pi_leibniz(double s, int &decimal_point){

    double int_part = floor(s);
    double float_part = s-int_part;
    decimal_point = 0;

    while(fabs(float_part) > 1e-9){
        float_part *= 10.0;
        int_part = floor(float_part);
        float_part -= int_part;
        decimal_point++;
    }

    double pi_series = 0.0;
    double x = 1.0;

    for(int i = 0; i < decimal_point; i++){
        pi_series += x/(2.0*i+1);
        x = -x;
    }

    double pi_value = 4*pi_series;
    return pi_value;

}

int main()
{
    double stop_at;
    cout<<"Input an approximate of pi value: "<<endl;
    cin>>stop_at;
    int decimal_point;
    double pi_approx = pi_leibniz(stop_at, decimal_point);
    cout<<setprecision(decimal_point)<<pi_approx<<endl;

    return 0;
}
