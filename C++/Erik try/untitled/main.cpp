#include <cstdlib>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
  ofstream outputFile;
  outputFile.open("oppgave_1b.txt");
  int n;
  n = 1000;
  double a[n], u[n],f[n], x[n], h, L, b[n], c[n];
  L = 1.0;
  h = L/(n-1);
  a[0] = 2;
  f[0] = 100;
  x[0] = 0;
  b[0] = -1;
  c[0] = -1;
  for (int i = 1; i < (n); i = i+1)
    {
      b[i] = -1;
      c[i] = -1;
      x[i] = x[i-1] + h;
      a[i] = 2 - b[i-1]*c[i-1]/a[i-1];
      f[i] = 100*exp (-10*x[i]) - f[i-1]*c[i-1]/a[i-1];
    }
  u[n-1] = f[n-1]*h*h/a[n-1];
  for (int i = (n-2); i >= 0; i = i-1)
    {
      u[i] = (f[i]*h*h - u[i+1]*b[i])/a[i];
      outputFile << setiosflags(ios::showpoint | ios::uppercase);
      outputFile << setprecision(10) << setw(20) << u[i] << endl;
    }
  outputFile.close();
  return 0;
}
