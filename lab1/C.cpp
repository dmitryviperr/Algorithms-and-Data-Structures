#include <iostream>
#include <vector> 
using namespace std;

void BubbleSort(vector<int>& A) {
    for (int iter = 0; iter < A.size() - 1; iter++) {
        bool swapped = false;
        for (int i = 0; i < A.size() - iter - 1; i++) {
            if (A[i] < A[i + 1]) {
                int temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}


int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }
    
    BubbleSort(A);
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }
    return 0;
}