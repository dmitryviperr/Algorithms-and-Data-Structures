#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void CountSort(vector<int>& A) {
    auto max_it = max_element(A.begin(), A.end());
    int k = *max_it;
    vector<int> cnt(k + 1, 0);
    for (int i = 0; i < A.size(); i++) {
        cnt[A[i]] ++;
    }
    A.clear();
    for (int num = 0; num < k + 1; num++) {
        A.insert(A.end(), cnt[num], num);
    }
}


int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }
    
    CountSort(A);
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }
    return 0;
}