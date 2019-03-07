#include <iostream>
#include <string>

using namespace std;
string s;
string p;
bool check(string a , string temp_p){
	int i;
	string temp_a ="";
	int qw = a.length();
	
	string mn ;
	for(i=0;i<qw;i++){
		mn = a[i];
		if (temp_p.find(a[i]) != std::string::npos) {
			int t  = temp_p.find(a[i]);
			temp_p.erase(t,1);
		}
		else if (mn != "?"){
			temp_a.append(mn);
		}
	}
	
	if (temp_a == ""){
		return true;
	}
	else{
		return false;
	}
			
			
}


int main(){
	cin >> s;
	cin >> p;
	int n = s.length();
	int m = p.length();
	int i;
	int res = 0;
	for (i = 0 ; i<=n-m ; i++){
		string temp = s.substr(i,m);
		
		if(check(temp,p)){
			res++;
			
		}
	}
	cout << res ;

}
