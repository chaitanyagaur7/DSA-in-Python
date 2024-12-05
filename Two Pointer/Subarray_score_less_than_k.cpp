#include <vector> 
#include <iostream> 

using namespace std;

int brute_force(vector<int> &nums, int goal) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int curr_sum = 0;
        int curr_score = 0;
        for (int j = i; j < nums.size(); j++) {
            curr_sum = curr_sum + nums[j];
            curr_score = curr_sum * (j-i+1);
            if (curr_score < goal) {
                count++;
            }
            else if (curr_score > goal) {
                break;
            }
        }
    }
    return count;
}

int sliding_window(vector<int> nums, int goal) {
    int left = 0;
    int count = 0;
    int sum = 0;
    int curr_score = 0;
    for (int right = 0; right < nums.size(); right ++) {
        sum = sum + nums[right];
        while ((sum * (right - left + 1)) >= goal && left <= right) {
            sum = sum - nums[left];
            left = left + 1;
        }
            count += right - left + 1;
        

    }
    return count;
}


int main() 
{
    vector <int> nums = {2,1,4,3,5};
    int count = 10;
    cout << sliding_window(nums,count) << endl;
    vector <int> vec = {1,1,1};
    count = 5;
    cout << sliding_window(vec,count) << endl;
    return 0;
}