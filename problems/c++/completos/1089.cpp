#include <iostream>
#include <vector>
#include <bits/stdc++.h> 
#include <algorithm>

using namespace std;

int main() {
  int n, entrada, max, pico, idx, nIdx;
  bool crescendo;
  vector<int> m;
  while ((cin >> n) && (n != 0)) {
    m.clear();
    while (n--) {
      cin >> entrada;
      m.push_back(entrada);
    }

    auto it = find(m.begin(), m.end(), *max_element(m.begin(), m.end()));

    max = distance(m.begin(), it);

    crescendo = false;
    pico = 1;

    for (int i = 0;i < m.size();i++) {
      idx = (max+i)%m.size();
      nIdx = (idx+1)%m.size();
      if (((m[nIdx]-m[idx]) > 0) != crescendo) {
        crescendo = !crescendo;
        pico++;
      }
    }
    cout << pico << endl;
  }
}
