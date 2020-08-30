#include<iostream>
#include<string>
using namespace std;
int main()
{
    int i,n,j;
    string str,st;
    char ch;
    cout<<"ENTER THE STRING PLEASE :";
    getline(cin,str);
    for(i=0;str[i]!='\0';i++)
    {
        if(str[i]>=65&&str[i]<=90)
        {
            n=str[i]-64;
            if((i+1)%2!=0)
            for(j=1;j<=n;j++)
            st=st+'#';
            else
            for(j=1;j<=n;j++)
            st=st+'$';
        }
        else if(str[i]>=97&&str[i]<=122)
        {
            n=str[i]-96;
            if((i+1)%2!=0)
            for(j=1;j<=n;j++)
            st=st+'#';
            else
            for(j=1;j<=n;j++)
            st=st+'$';
        }
    }
    cout<<"THE ENCRYPTED STRING IS :"<<st;
    return 0;
}
