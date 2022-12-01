#include <iostream>
using namespace std;

int main()
{
    int T, k, n;
    cin >> T;

    for (int i = 0; i < T; i++)
    { ///
        cin >> k;
        cin >> n;
        int person[k][n] = {
            0,
        };
        for (int a = 0; a <= k; a++)
        {
            for (int b = 0; b <= n; b++)
            {
                person[0][b] = b;
                person[a][1] = 1;
            }
        } //초기화

        for (int a = 1; a <= k; a++)
        {
            for (int b = 2; b <= n; b++)
            {
                //반복문
                person[a][b] = person[a - 1][b] + person[a][b - 1];
            }
        }
        cout << person[k][n];
    }
}