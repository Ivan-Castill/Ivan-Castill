#include <iostream>
#include <cmath>
#include <string>
using namespace std;
//comenzo la prueba...
void ejercicio1() {
    int numero;
    cout << "Ingrese un numero impar mayor a uno: ";
    cin >> numero;
    if (numero <= 1 || numero % 2 == 0) {
        cout << "El numero ingresado no es impar o no es mayor a uno." << endl;
        return;
    } 
    for (int i = 0; i <= numero / 2; i++) {
        for (int l = 0; l < (numero / 2 + 1) - i; l++) cout << "-";
        for (int j = 0; j < 2 * i + 1; j++) cout << "*";
        
        for (int k = 0; k < (numero / 2 + 1) - i; k++) cout << "+";
        cout << endl;
    }
    for (int i = 1; i <= numero / 2; i++) {
        for (int l = 0; l < i+1; l++) cout << "-";
        for (int j = 0; j < numero - 2 * i; j++) cout << "*";
        for (int k = 0; k < i+1; k++) cout << "+";
        cout << endl;
    }
}


//void ejercicio1(){
//	int numero;
//	cout<<"Ingrese un numero impar mayor a uno: ";
//	cin>>numero;
//	for (int i=0 ; i <=numero/2 ; i++){
//		
//		for(int l=(numero/2+1)-i;l>1;l--)cout<<"-";
//		for(int j=0; j<2*i+1;j++)cout<<"*";
//		for(int k=(numero/2+1)-i;k>1;k--)cout<<"+";
//		
//		cout<<endl;
//	}
//	for (int i=0;i<numero/2;i++){
//		for(int l=0; l<i+1;l++)cout<<"-";
//		for(int j=numero; j>2*(i+1);i--)cout<<"*";
//		for(int k=0; k<i+1;k++)cout<<"+";
//		
//		cout<<endl;
//	}
//	
//}
void ejercicio2(){
	int num;
	cout<<" Ingrese un numero positivc mayor igual a 2: ";
	cin>>num;
	for (int i=0;i<=num;i++){
		if (i==0||i==num){
			for(int l=0;l<=num;l++)cout<<"*";
		}
		else{
			for(int l=0;l<=num;l++){
				if(l==0||l==num){cout<<"*";}
				else{cout<<"+";}
			}
		}
		cout<<endl;
	}
}
void ejercicio3(){
	string palabra;bool palindromo=true;
	cout<<"Ingrese una palabra sin espacios en blancos: ";
	cin>>palabra;
	for(int i=0;i<palabra.length();i++){
		if(palabra[i]!=palabra[palabra.length()-i-1]) palindromo=false;
	}
	cout<<"Numero de caracteres:"<<palabra.length()<<endl;
	if (palindromo){cout<<"Es palindromo";}
	else{cout<<"NO es palindromo";}
	
}
void ejercicio4(){
	int num;
	cout<<"Ingrese un numero entero: ";cin>>num;
	while(num>0){
		cout<<" "<<num%2<<endl;
		num=num/2;
	}
	cout<<"Por favor;LEA EL BINARIO DESDE ABAJO HACIA ARRIBA ^^ ";
}
//se cabo la prueba...

//ejrcicio por punto
void punto_extra(){
	
}


int main(){
//	ejercicio4();
//	ejercicio3();
	ejercicio2();
//	ejercicio1();
	return 0;
	
}
