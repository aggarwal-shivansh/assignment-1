#include<iostream>
#include<string>
#include<conio.h>
using namespace std;
int main()
{
    char ch;
    int i;
    string str;
    do
    {
    cout<<"ENTER 1 FOR ENCRYPTION "<<endl<<"ENTER 2 FOR DECRYPTING THE STRING"<<endl<<"ENTER YOUR CHOICE PLEASE"<<endl;
    ch=getche();
     switch(ch)
     {
         case '1':
         cout<<endl<<"ENTER THE STRING PLEASE :";
         getline(cin,str);
         for(i=0;str[i]!='\0';i++)
         {
             str[i]+=5;
         }
         cout<<"THE ENCRYPTED STRING IS : " <<str<<endl;
         break;
         case '2':
         cout<<endl<<"ENTER THE STRING PLEASE :";
         getline(cin,str);
         for(i=0;str[i]!='\0';i++)
         {
             str[i]-=5;
         }
         cout<<"THE DECRYPTED STRING IS : "<<str<<endl<<endl;
         break;
         default:
         cout<<endl<<"WRONG CHOICE \n THANK YOU ! ";
     }
    }while(ch=='1'||ch=='2');
    return 0;
}
