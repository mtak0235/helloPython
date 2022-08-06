#include <vector>
#include <iostream>
#include <algorithm>
int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int n;
	std::cin >> n;
	std::vector<int> l;
	for (int i = 0; i < n; i++) {
		int t;
		std::cin >> t;
		l.push_back(t);
	}
		std::sort(l.begin(), l.end());
	std::cout << l.front() <<" "<< l.back() << std::endl;
}
