#include <bits/stdc++.h>
using namespace std;


int main()
{
    char c ='a';
    int n , m, numBar, t;
    cin>>n>>m>>numBar>>t;
    char map[n][m];
    for (int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            map[i][j] = '+';

    while(numBar -- )
    {
        int i, j;
        i = rand() % n;
        j = rand() % m;
        map[i][j] = '#';
    }
    while(t -- )
    {
        int i, j;

        i = rand() % n;
        j = rand() % m;
        map[i][j] = c;
        c = char(int(c) + 1);
        if(int(c) == 123)
            c = 'A';
    }
    map[rand() % n][rand() % m] = '$';
     ofstream MyFile("data.txt");
     for (int i = 0; i < n; i++){
         for(int j = 0; j < m; j++)
            MyFile << map[i][j];
         MyFile<<"\n";
     }



    return 0;
}
