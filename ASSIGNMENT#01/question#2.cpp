#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    char str1[20];
    int i,j,l=0,f=0;
    cout<<"ENTER THE STRING";
    cin>>str1;
    l=strlen(str1)-1;
    for(i=l,j=0;i>=l/2;i--,j++)
    {
        if(str1[i]!=str1[j])
     {
         f=1;
        break;
     }
    }
    if(f==0)
    cout<<"YES THE STRING IS PALLINDROME";
    else
    cout<<"NO THE STRING IS NOT PALLINDROME";
return 0;
}

