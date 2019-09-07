#include <cmath>    //Math
#include <iostream> //Input output
#include <cstdlib>  // atof (ASCII to float conversion)
#include <vector>
#include <fstream> //Lese/skrive filer
#include <iomanip> //Formatere output med setw og setprecision
#include <cmath>

using namespace std;


void tdma(const vector<double>& a,
          const vector<double>& b,
          const vector<double>& c,
          const vector<double>& d,
          vector<double>& f){
  size_t N = d.size();


  //Creating vectors
  vector<double> c_star(N, 0.0);
  vector<double> d_star(N, 0.0);

  //Update coefficients in the first row
  c_star[0] = c[0] / b[0];
  d_star[0] = d[0] / b[0];

  //Create the c_star and d_star coefficients in the forward sweep

  for (int i=1; i<N; i++) {
    double m = 1.0 / (b[i] - a[i-1] * c_star[i-1]);
    c_star[i] = c[i] * m;
    d_star[i] = (d[i] - a[i-1] * d_star[i-1]) * m;
  }

  //Reverse sweep
  for (int i=N-1; i-- >0; ) { //Kunne vi skrevet i>0;i-- her?
    f[i] = d_star[i] - c_star[i] * f[i+1];
  }
}

ofstream ofile;

void print(std::vector <double> const &a) {
   std::cout << "The vector elements are : ";

   for(int i=0; i < a.size(); i++)
      std::cout << a.at(i) << ' ';
}


int main ()
{
  size_t N = 1000;

  vector<double> a(N, -1);
  vector<double> b(N, 2);
  vector<double> c(N, -1);

  vector<double> d(N, 0.0);
  vector<double> x(N, 0.0);
  vector<double> f(N, 0.0);
  vector<double> anal(N, 0.0);

  double h = (1-0)/double(N);
  for (int i=1; i<N; i++){
    x[i] = x[i-1]+h;
  }
  for (int i=0; i<N; i++){
    d[i] = pow(h,2) * 100 * exp(-10 * x[i]);
    anal[i] = 1-(1-exp(-10)) * x[i] - exp(-10 * x[i]);
  }

  tdma(a,b,c,d,f);
  ofile.open("results");
  for (int i=0; i<N; i++){
    ofile << setw(15) << setprecision(8) << x[i] << " " << f[i] << " "<< anal[i]<< endl;
  }
  ofile.close();
  system("python3 Plotter.py results");
  return 0;



}
