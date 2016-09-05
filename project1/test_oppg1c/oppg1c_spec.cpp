#include <iostream>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <time.h>
using namespace std;

int main()
{
    ofstream outputFile;
    outputFile.open("oppgave_1b.txt");
    int n;
    n = 1e5;
    double a[n], u[n],f[n], x[n], h, L, b[n], c[n], t, sec;
    L = 1.0;
    h = L/(n-1);
    a[0] = 2;
    f[0] = 100;
    x[0] = 0;

    clock_t start, finish;  //start and final time
    start = clock();
    for (int i = 1; i < (n); i = i+1)

      {
        x[i] = x[i-1] + h;
        a[i] = 2 - 1/a[i-1];
        f[i] = 100*exp (-10*x[i]) + f[i-1]/a[i-1];
      }

    u[n-1] = f[n-1]*h*h/a[n-1];
    for (int i = (n-2); i >= 0; i = i-1)

      {
        u[i] = (f[i]*h*h + u[i+1])/a[i];
        outputFile << setiosflags(ios::showpoint | ios::uppercase);
        outputFile << setprecision(10) << setw(20) << u[i] << endl;
      }

    outputFile.close();
    finish=clock();
    t = (finish-start);
    sec = t/CLOCKS_PER_SEC;
    cout << t << endl;
    cout << CLOCKS_PER_SEC << endl;
    cout << sec << endl;
}
