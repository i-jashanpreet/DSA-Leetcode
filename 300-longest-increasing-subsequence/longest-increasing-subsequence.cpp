
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        vector<vector<int>> dp(n, vector<int>(n + 1, -1));

        function<int(int, int)> f = [&](int i, int prev) {
            if (i == n) {
                return 0;
            }

            if (dp[i][prev + 1] != -1) {
                return dp[i][prev + 1];
            }

            int take = 0;

            if (prev == -1 || nums[i] > nums[prev]) {
                take = 1 + f(i + 1, i);
            }

            int not_take = f(i + 1, prev);

            int ans = max(take, not_take);

            return dp[i][prev + 1] = ans;
        };

        return f(0, -1);
    }
};
