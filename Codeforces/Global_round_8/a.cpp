#include<bits/stdc++.h>
using namespace std;
 
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
typedef long long ll;

int main(){
    int t;
    cin>>t;
    while (t--){
        ll a, b, n;
        cin>>a>>b>>n;

        if (a>b) swap(a, b);
        
        ll temp;
        int numops = 0;
        while (b<=n){
            temp = b;
            b = a + b;
            a = temp;
            numops++;
            // cout<<a<<" "<<b<<endl;
        }
        cout<<numops<<endl;
    }
}