#include <iostream>
#include <vector> 
using namespace std;

int BubbleSortCount(vector<int>& A, int N) {
    int cnt = 0;
    for (int iter = 0; iter < N - 1; iter++) {
        bool swapped = false;
        for (int i = 0; i < N - iter - 1; i++) {
            if (A[i] > A[i + 1]) {
                int temp = A[i];
                A[i] = A[i + 1];
                A[i + 1] = temp;
                swapped = true;
                cnt++;
            }
        }
        if (!swapped) {
            break;
        }
    }
    return cnt;
}


int main() {
    vector<int> A;
    int x;
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> x;
        A.push_back(x);
    }
    
    int result = BubbleSortCount(A, N);
    cout << result << endl;
    return 0;
}