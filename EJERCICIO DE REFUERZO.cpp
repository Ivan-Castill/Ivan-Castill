#include <iostream>
using namespace std;
void ejercicio1() {
    int numero;
    cout << "Ingrese un numero impar mayor a uno: ";
    cin >> numero;
    if (numero <= 1 || numero % 2 == 0) {
        cout << "El numero ingresado no es impar o no es mayor a uno." << endl;
        return;
    } 
    for (int i = 0; i <= numero / 2; i++) {
        for (int l = 0; l < (numero / 2 + 1) - i - 1; l++) cout << " ";
        cout << "*";
        if (i > 0) {
            for (int j = 0; j < 2 * i - 1; j++) cout << " ";
            cout << "*";
        }
        for (int k = 0; k < (numero / 2 + 1) - i - 1; k++) cout << " ";
        cout << endl;
    }
    for (int i = 1; i <= numero / 2; i++) {
        for (int l = 0; l < i; l++) cout << " ";
        cout << "*";
        for (int j = 0; j < numero - 2 * i - 2; j++) cout << " ";
        if (i < numero / 2) cout << "*";
        for (int k = 0; k < i; k++) cout << " ";
        cout << endl;
    }
}
int main(){
	ejercicio1();
	return 0;
}

