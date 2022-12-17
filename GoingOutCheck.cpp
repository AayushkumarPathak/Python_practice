#include<iostream>
using namespace std;

int main(){
    int date;
    int money;
    cout<<"Enter the date: ";
    cin>>date;
    cout<<"Enter the pocket money: ";
    cin>>money;
    for(date=1;date<=28;date++){
        if(date%2==0){
            continue;
        }
        if (money==0){
            break;
        }
        cout<<"Go Out to Enjoy!"<<endl;
        money=money-300;
    
        
    }
    return 0;
}
