#include <iostream>
#include <vector>
using namespace std;

void selection_sort(vector<int>& A) {
    int size = A.size();
    for (int i = 0; i < size - 1; i++) {
        int key = A[i];
        int ind = i;
        for (int j = i + 1; j < size; j++) {
            if (A[j] > key) {
                key = A[j]; 
                ind = j;
            }
        }
        if (i != ind) {
            int temp = A[i];
            A[i] = A[ind];
            A[ind] = temp;
        }
    }
}


int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }
    
    selection_sort(A);
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }
    return 0;
}