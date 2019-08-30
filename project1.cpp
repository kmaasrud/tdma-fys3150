#include <cmath>
#include <iostream>
#include <vector>

// Vectors a, b, c and d are const. They will not be modified
// by the function. Vector f (the solution vector) is non-const
// and thus will be calculated and updated by the function.
void thomas_algorithm(const std::vector<double>& a,
                      const std::vector<double>& b,
                      const std::vector<double>& c,
                      const std::vector<double>& d,
                      std::vector<double>& f) {
  size_t N = d.size();

  // Create the temporary vectors
  // Note that this is inefficient as it is possible to call
  // this function many times. A better implementation would
  // pass these temporary matrices by non-const reference to
  // save excess allocation and deallocation
  std::vector<double> c_star(N, 0.0);
  std::vector<double> d_star(N, 0.0);

  // This updates the coefficients in the first row
  // Note that we should be checking for division by zero here
  c_star[0] = c[0] / b[0];
  d_star[0] = d[0] / b[0];

  // Create the c_star and d_star coefficients in the forward sweep
  for (int i=1; i<N; i++) {
    double m = 1.0 / (b[i] - a[i] * c_star[i-1]);
    c_star[i] = c[i] * m;
    d_star[i] = (d[i] - a[i] * d_star[i-1]) * m;
  }

  // This is the reverse sweep, used to update the solution vector f
  for (int i=N-1; i-- > 0; ) {
    f[i] = d_star[i] - c_star[i] * d[i+1];
  }
}

// Although thomas_algorithm provides everything necessary to solve
// a tridiagonal system, it is helpful to wrap it up in a "real world"
// example. The main function below uses a tridiagonal system from
// a Boundary Value Problem (BVP). This is the discretisation of the
// 1D heat equation.
int main(int argc, char **argv) {

  // Create a Finite Difference Method (FDM) mesh with 13 points
  // using the Crank-Nicolson method to solve the discretised
  // heat equation.
  size_t N = 13;
  double delta_x = 1.0/static_cast<double>(N);
  double delta_t = 0.001;
  double r = delta_t/(delta_x*delta_x);

  // First we create the vectors to store the coefficients
  std::vector<double> a(N-1, -r/2.0);
  std::vector<double> b(N, 1.0+r);
  std::vector<double> c(N-1, -r/2.0);
  std::vector<double> d(N, 0.0);
  std::vector<double> f(N, 0.0);

  // Fill in the current time step initial value
  // vector using three peaks with various amplitudes
  f[5] = 1; f[6] = 2; f[7] = 1;

  // We output the solution vector f, prior to a
  // new time-step
  std::cout << "f = (";
  for (int i=0; i<N; i++) {
    std::cout << f[i];
    if (i < N-1) {
      std:: cout << ", ";
    }
  }
  std::cout << ")" << std::endl << std::endl;

  // Fill in the current time step vector d
  for (int i=1; i<N-1; i++) {
    d[i] = r*0.5*f[i+1] + (1.0-r)*f[i] + r*0.5*f[i-1];
  }

  // Now we solve the tridiagonal system
  thomas_algorithm(a, b, c, d, f);

  // Finally we output the solution vector f
  std::cout << "f = (";
  for (int i=0; i<N; i++) {
    std::cout << f[i];
    if (i < N-1) {
      std:: cout << ", ";
    }
  }
  std::cout << ")" << std::endl;

  return 0;
}
