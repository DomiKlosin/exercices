#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <random>
#include <ctime>
#include <cstdlib>

using namespace std;

int random_int(int min, int max){
    static std::default_random_engine e{static_cast<long unsigned int>(std::time(0))};
    std::uniform_int_distribution<int> d{min, max};
    return d(e);
}

int binarySearch() {
    int size_num = 30;
    vector<int> numbers(size_num);

    for(int i=0; i<size_num; i++){
        numbers[i] = random_int(0, 99);
    }

    sort(numbers.begin(), numbers.end());

    int start_index = 0;
    int end_index = size_num - 1;
    int last_mid_index = -1;

    while(start_index <= end_index){
        int mid_index = (end_index + start_index) / 2;

        if (mid_index == last_mid_index) {
            return -1;
        }

        last_mid_index = mid_index;

        cout << "Is this your number: " << numbers[mid_index] << endl;
        cout << "0 - your number is lower" << endl;
        cout << "1 - it's your number" << endl;
        cout << "2 - your number is higher:" << endl;

        int user_choice;
        cin >> user_choice;

        if(user_choice == 1){
            return mid_index;
        }
        else if(user_choice == 0){
            end_index = mid_index - 1;
        }
        else if(user_choice == 2){
            start_index = mid_index + 1;
        }
        else{
            cout <<"Invalid input"<<endl;
        }
    }
}

int main() {

    int result = binarySearch();
    if(result != -1){
        cout<<"Found at index: "<<result<<endl;
    }
    else{
        cout<<"Number not found in the set"<<endl;
    }

    return 0;
}
