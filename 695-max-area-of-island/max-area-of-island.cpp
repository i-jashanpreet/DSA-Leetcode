
class Solution {
public:
    int m, n;

    int f(int i, int j, vector<vector<int>>& grid) {
        if (i >= m || i < 0 || j >= n || j < 0)
            return 0;

        if (grid[i][j] == 0)
            return 0;

        grid[i][j] = 0;  // Mark visited

        int area = 1;
        area += f(i - 1, j, grid);
        area += f(i + 1, j, grid);
        area += f(i, j - 1, grid);
        area += f(i, j + 1, grid);

        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        int maxi = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxi = max(maxi, f(i, j, grid));
                }
            }
        }

        return maxi;
    }
};
