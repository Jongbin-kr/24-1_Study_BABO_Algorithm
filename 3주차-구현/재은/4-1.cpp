#include <iostream>
using namespace std;

int n;
string plans;
int x = 1, y = 1;

// directions
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char directions[4] = {'L', 'R', 'U', 'D'};

// 이동한 위치
int new_x = 0, new_y = 0;

int main()
{
    cin >> n;
    cin.ignore();
    getline(cin, plans);
    for (int i = 0; i < plans.size(); i++)
    {
        char move = plans[i]; //'L', 'R', 'U', 'D' 중 하나의 값
        int index = 0;
        for (int j = 0; j < 4; j++)
        {
            if (directions[j] == move)
                break;
            else
            {
                index += 1;
                continue;
            }
        }

        new_x = x + dx[index], new_y = y + dy[index];
        if (new_x < 1 || new_y < 1 || new_x > n || new_y > n)
            continue;
        x = new_x, y = new_y;
    }

    cout << x << ' ' << y;
}