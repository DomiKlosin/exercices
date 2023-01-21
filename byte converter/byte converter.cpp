#include <iostream>

using namespace std;

class Byte{
public:
    long long b;
    int b2;
    int kb;
    int mb;
    int gb;
    int tb;
    const int st=1024;

    Byte(): b(0){
    cout<<"Constructor\n";}
    ~Byte(){
    cout<<"Destructor\n";}

    long long take(){
    cout<<"Input number of bytes: ";
    cin>>b;
    return b;}

    int calculateKB(){
    kb=b/st;
    return tb;}

    int calculateMB(){
    mb=kb/st;
    return mb;}

    int calculateGB(){
    gb=mb/st;
    return gb;}

    int calculateTB(){
    tb=gb/st;
    return tb;}

    void write(){
    cout<<b<<" B is "<<tb<<"TB, "<<gb<<" GB, "<<mb<<" MB, "<<kb<<" KB"<<endl;}
};
int main()
{
    Byte ob;
    ob.take();
    ob.calculateKB();
    ob.calculateMB();
    ob.calculateGB();
    ob.calculateTB();
    ob.write();

    return 0;
}
