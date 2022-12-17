#include<iostream>
using namespace std;

int sum(int a, int b){
    int c=a+b;
    return c;
}
void swap(int a, int b){
    int temp = a;
    a=b;
    b=temp;
}
int main(){
    int a=4,b=5;
    //call by value
    //cout<<"The Sum is:"<<sum(5,6)<<endl;

    cout<<"The value of a is:"<<a<<"The value of b is:"<<b<<endl;
    swap(a,b);
    cout<<"The value of a is:"<<a<< "The value of b is:"<<b<<endl;

    return 0;
}