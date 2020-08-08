#include<iostream>
using namespace std;
int main()
{
    int a,b,c,i,j;
    cout<<"ENTER THE RANGE IN WHOLE NO. i.e a AND b";
    cin>>a>>b;
    cout<<"PRIME NUMBERS ARE :"<<endl;
    for(i=a;i<=b;i++)
    {
        c=0;
        for(j=1;j<=i;j++)
        {
            if(i%j==0)
            c++;
        }
        if(c==2)
        cout<<i<<endl;

    }

    return 0;
}
