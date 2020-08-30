#include<iostream>
using namespace std;
int main(int n,char *c[])
{
    int i,min,arr[n];
    for(i=0;i<n;i++)
    {
        arr[i]=(int)c[i];
    }
    min=arr[0];
    for(i=1;i<n;i++)
    {
        if(min>arr[i])
        min=arr[i];
    }
    cout<<"THE SMALLEST NUMBER IS :"<<min;
    return 0;
}
