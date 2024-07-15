#include <iostream>
using namespace std;
struct MyClass{
    int a = 0;
    MyClass(int a, int b): a(a){
        cout<<"MyClass constructor"<<endl;
    }
    MyClass(char a): a(a){
        cout<<"MyClass constructor"<<endl;
    }
    MyClass() {
        cout<<"MyClass constructor"<<endl;
    }

};



struct AnotherClass{
    MyClass obj;
    int k;
    AnotherClass(int a): obj(1,2), k(1){
        cout<<"AnotherClass constructor"<<endl;
    }
};


int main(){

    AnotherClass obj(10);

    return 0;
}