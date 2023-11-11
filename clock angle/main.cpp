#include <iostream>
#include <math.h>

using namespace std;

double check_angle(string& time){

    string hour_str = time.substr(0,2);
    string minute_str = time.substr(3,2);
    char format = time.back();

    int hour = stoi(hour_str);
    int minute = stoi(minute_str);

    double hour_angle = 0.5*(60*hour+minute);
    double minute_angle = 6*minute;
    double angle = abs(hour_angle-minute_angle);

    if(angle>180){
        angle = 360-angle;
    }
    if(format == 'r'){
        angle = angle*M_PI/180.0;
    }

    return angle;
}

int main()
{
    string input;
    double angle;
    cout<<"Input time in format hh:mmf (hh - hours, mm - minutes, f - format: r-radians, d-degrees)"<<endl;
    cin >> input;
    angle = check_angle(input);
    cout<<angle<<endl;

    return 0;
}

