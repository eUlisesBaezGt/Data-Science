#include <iostream>
#include <cstdlib>
using namespace std;

const int nCities = 2; //Filas
const int nMonths = 6; //Columnas

int main() {
    int temperature[nCities][nMonths];
    cout << "Ingresa las temperaturas de 2 ciudades durante 6 meses:\n";
    for (int i = 0; i < nCities; ++i) //Filas
    {
        for (int j = 0; j < nMonths; ++j) //Columnas
        {
            temperature[i][j]= 1 + (rand() % 40);
        }
    }
    cout << "\n\nMostrando Valores:\n";
    for (int i = 0; i < nCities; ++i)
    {
        for (int j = 0; j < nMonths; ++j)
        {
            cout << "Ciudad " << i + 1 << ", Dia " << j + 1 << " = " << temperature[i][j] << endl;
        }
    }
    return 0;
}
