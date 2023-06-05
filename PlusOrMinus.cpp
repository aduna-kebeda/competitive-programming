#include <iostream>
using namespace std;


int main(){
    
int a, b, c, n;
cin>>n;
for(int i=0; i<n; i++){
cin >> a >> b >> c ;
if(c==(a+b))
cout<<"+"<<endl;
else if(c==(a-b))
cout<<"-"<<endl;
}
    return 0;
}
