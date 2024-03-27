#include <iostream>
using namespace std;

string location;
int x = 1, y = 1;

// directions
int dx[8] = {-2, 2, -2, 2, -1, 1, -1, 1};
int dy[8] = {-1, -1, 1, 1, -2, -2, 2, 2};

int main()
{
    cin >> location;
    // 아스키코드 적용해서 int로 변환
    int row = location[1] - '0';
    int col = location[0] - 'a' + 1;
    int new_x = 0, new_y = 0;
    int cnt = 0;
    for (int i = 0; i < 8; i++)
    {
        new_x = row + dx[i];
        new_y = row + dy[i];
        if (new_x >= 1 && new_x <= 8 && 1 <= new_y && new_y <= 8)
        {
            cnt += 1;
        }
    }

    cout << cnt;
}