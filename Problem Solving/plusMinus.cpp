//Solved using HackerRank https://www.hackerrank.com/challenges/plus-minus/problem
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

void plusMinus(vector<int> arr) {
    int negatives = 0;
    int positives = 0;
    int zeros = 0;
    
    for (int i:arr)
    {
        if(i<0){
            negatives++;
        }
        if(i>0){
            positives ++;
        }
        
        if(i==0){
            zeros++;
        }
    }
    
    float negative_ratios = static_cast<float>(negatives) / arr.size();
    float positive_ratios = static_cast<float>(positives) / arr.size();
    float zero_ratio = static_cast<float>(zeros) / arr.size();
    
   cout<<positive_ratios<<endl;
   cout<<negative_ratios<<endl;
   cout<<zero_ratio<<endl;

}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    plusMinus(arr);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
