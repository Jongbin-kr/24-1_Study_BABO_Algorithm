#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> yen = {500, 100, 50, 10, 5, 1};
    int change, count = 0;
    int k;
    cin >> k;
    change = 1000 - k;

    for (int i = 0; i < 6; i++)
    {
        for (;;)
        {
            if (change >= yen[i])
            {
                change -= yen[i];
                count++;
            }
            else
                break;
        }
    }
    cout << count;
}