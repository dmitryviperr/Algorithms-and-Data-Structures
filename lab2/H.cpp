#include <iostream>
#include <algorithm>
using namespace std;

bool good(long long x, long long w, long long h, long long n) {
    long long cnt_w = x / w;
    long long cnt_h = x / h;
    if (cnt_w == 0 || cnt_h == 0) return n == 0;
    return cnt_w >= (n + cnt_h - 1) / cnt_h;
}

int main() {
    long long w, h, n;
    cin >> w >> h >> n;
    
    long long l = 0;
    long long r = 1;
    while (!good(r, w, h, n)) r *= 2;
    
    while (r - l > 1) {
        long long m = (l + r) / 2;
        if (good(m, w, h, n)) {
            r = m;
        } else {
            l = m;
        }
    }
    cout << r << endl;
    return 0;
}