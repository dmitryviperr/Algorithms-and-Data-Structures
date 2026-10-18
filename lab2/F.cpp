#include <iostream>
using namespace std;

bool good(int cnt, int q, int s, int t) {
    return t / q + t / s >= cnt;
} 


int main(){
    int N, x, y;
    cin >> N >> x >> y;
    if (x > y) {
        int temp = x;
        x = y;
        y = temp;
    }

    int l = 0;
    int r = (N - 1) * y;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (!good(N - 1, x, y, m)){
            l = m;
        } else {
            r = m;
        }
    }
    int result = r + x;
    cout << result << endl;
    return 0;
}
