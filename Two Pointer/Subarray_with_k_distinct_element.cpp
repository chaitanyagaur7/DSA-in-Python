#include <iostream> 
#include <vector> 
#include <set> 
#include <unordered_map>
using namespace std;

int brute_force(vector<int> nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        set<int> s;
        for (int j = i; j < nums.size();j++) {
            s.insert(nums[j]);
            if (s.size() == k) {
                count++;
            }
        }
    }
    return count;

}

int sliding_window(vector<int> nums, int k) {
    int left = 0;
    int count = 0;
    unordered_map<int,int> map;
    for (int right = 0; right < nums.size(); right++) {
        map[nums[right]]++;
        while (map.size() > k) {
            map[nums[left]] -= 1;
            if (map[nums[left]] == 0) {
                map.erase(nums[left]);
            }
            left++;
        }
        if (map.size() == k) {
            count += (right - left + 1);
        }
    }
    return count;
}


int main() {
    vector <int> v = {1,2,1,2,3};
    int k = 2;
    cout << abs(sliding_window(v,k) - sliding_window(v,k-1)) + 1<< endl;
    vector <int> nums = {1,2,1,3,4};
    k = 3;
    cout << abs(sliding_window(nums,k) - sliding_window(nums,k-1)) + 1 << endl;
    return 0;

}