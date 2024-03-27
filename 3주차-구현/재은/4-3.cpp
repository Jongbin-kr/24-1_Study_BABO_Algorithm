#include <iostream>
#include <string>
using namespace std;

int hour, cnt;

bool checkThree(int h, int m, int s)
{
    string m_str = to_string(m), s_str = to_string(s);
    if (h % 10 == 3 || m_str[0] % 10 == 3 || m_str[1] % 10 == 3 || s_str[0] % 10 == 3 || s_str[1] % 10 == 3)
        return true;
    return false;
}

int main()
{
    cin >> hour;
    int cnt = 0;
    for (int i = 0; i <= hour; i++)
    {
        for (int j = 0; j < 60; j++)
        {
            for (int k = 0; k < 60; k++)
            {
                if (checkThree(i, j, k))
                {
                    cnt += 1;
                }
            }
        }
    }

    cout << cnt;
}