#include <iostream>
#include <vector>
using namespace std;

bool good(double x, vector<int>& a, int k) {
    int cnt = 0;
    for (int i = 0; i < a.size(); i++) {
        cnt += a[i] / x;
    }
    return cnt >= k;
}


int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l = 0;
    long long r = 10e10 + 1;
    for (int i = 0; i < 100; i++) {
        double m = (l + r) / 2;
        if (good(m, a, k)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << l << endl;
    return 0;
}