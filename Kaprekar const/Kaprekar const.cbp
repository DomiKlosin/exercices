#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

int user_num, max_num, min_num;
string str_num1, str_num2;
const int Kaprekar_const = 6174;

int main()
{
    cout<<"Input a four-digit number with at least two digits that are different:"<<endl;
    cin>>user_num;

    while(user_num != Kaprekar_const)
    {
        str_num1 = to_string(user_num);
        str_num2 = to_string(user_num);

        sort(str_num1.begin(), str_num1.end());
        reverse(str_num1.begin(), str_num1.end());
        sort(str_num2.begin(), str_num2.end());

        max_num = stoi(str_num1);
        min_num = stoi(str_num2);

        user_num = max_num - min_num;

        cout<<max_num<<" - "<<min_num<<" = "<<user_num<<endl;
    }
    return 0;
}
