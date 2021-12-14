#include <map>
#include <cmath>
#include <queue>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <algorithm>
using namespace std;
#define x first
#define y second
#define PI acos(-1)
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define ll long long
#define ld long double
#define ii pair<int,int>
#define flush cout.flush()
#define all(k) k.begin(),k.end()
#define rall(k) k.rbegin(),k.rend()
#define db(x) cerr<<#x<<" = "<<x<<endl
#define PREC cout << fixed << setprecision(48)



void apply (string &pattern, map<pair<char,char>, char> &productions){

    string newPattern;
    newPattern += pattern[0];
    for(int i = 1; i < pattern.size(); i++){
       pair<char,char> curr = {newPattern.back(), pattern[i]};
        if(productions.count(curr)){
            newPattern.push_back(productions[curr]);
        }
        newPattern.push_back(pattern[i]);
    }
    pattern = newPattern;
}
int32_t main(){
    ios::sync_with_stdio(0); cin.tie(0);
    string pattern;
    map<pair<char,char>, char> productions;

    cin >> pattern;
    cout << pattern << endl;

    char produce;
    pair<char,char> pear;

    while(cin >> pear.first >> pear.second){
        string arrow; cin >> arrow;
        cin >> produce;

        productions[pear] = produce;
    }

    for(int i = 0; i < 10; i++){
        apply(pattern, productions);
        //cout << pattern << endl;
    }

    map<char, int> freq;
    for(char c : pattern) freq[c]++;
    int mx = -1, mn = 11111111;
    for(auto &[c,f] : freq){
        mx = max(mx, f);
        mn = min(mn, f);
    }

    cout << mx - mn << endl;

}
