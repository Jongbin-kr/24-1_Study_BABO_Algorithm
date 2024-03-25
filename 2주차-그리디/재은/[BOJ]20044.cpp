#include <iostream>
#include <algorithm>
using namespace std;

void get_min(int *arr, int n)
{
    int minVal = arr[0];
    for (int i = 0; i < n; i++)
    {
        minVal = min(minVal, arr[i]);
    }
    cout << minVal;
}

int main()
{
    int N;
    cin >> N;

    int *A = new int[N * 2];

    for (int i = 0; i < N * 2; i++)
    {
        cin >> A[i];
    }

    sort(A, A + N * 2);

    int *result = new int[N];

    for (int i = 0; i < N; i++)
    {
        result[i] = A[i] + A[2 * N - i - 1];
    }
    get_min(result, N);
}