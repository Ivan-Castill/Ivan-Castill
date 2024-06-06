#include <iostream>
#include <string>
#include <cmath>
#include <cstring>//para manipular strings tipo arreglos de char
using namespace std;
/*
//funcion secundaria
double sumar(double n1,double n2){
	
	return n1+n2;
} 


void saludar_persona(string nombre){
	cout<<"hola"<<nombre<<endl;
	
}

double obtener_PI(){
	return M_PI;
}

void saludar(){
	cout<<"hola mundo";
}
*/

void forma1(){
	char palabra[]="hola";
	cout<<"longitud de la palabra: "<<strlen(palabra)<<endl;//una forma 
}
void forma2(){
	string palabra="desktopclase";
	cout<<"longitud de la palabra: "<<palabra.length()<<endl;
}

void dividir_caracteres(){
	string palabra="";
	cout<<"ingrese la palabra: ";cin>>palabra;
	cout<<"Deletreando la palabra \""<<palabra<<"\":"<<endl;
	for(size_t i=0;i<palabra.length();++i){
		cout<<palabra[i]<<endl;
	}
}
/*
void Verificacion_correo(){
	string correo="";
	char c='@';
	char g='.';
	cout<<"ingrese el correo: ";
	cin>>correo;
	if(correo.find(c,g) != string::npos){ //determina si encotro ese caracter
		cout<<"correo valido";
	}
	else if(correo.find(c)==1){
		cout<<"correo no valido";
	}
	else if(correo.find(c)<1){
		cout<<"correo no valido.";
	}
	
}
*/
string Verificacion_correo2(string correo){
	int arroba=0;
	int punto=0;
	for(size_t i=0;i<correo.length();++i){
		if(correo[i]=='@'){
			arroba++;
		}else if(correo[i]=='.'){
			punto++;
		}
	}
	if(arroba==1){
		return"correo Valido";
	}else if(punto>1){
		return"Correo mal ingresado";
	}
	else{
		return"Correo mal ingresado";
	}
}
int main(){
	string correo;
	cout<<"ingrese un correo"<<endl;
	cin>>correo;
	cout<<Verificacion_correo2(correo)<<endl;	/*
	double r=sumar(4.5,5.1);
	cout<<"resultado: "<<r;
	*/
	//Verificacion_correo2();
	//dividir_caracteres();
	//forma1();	
	//forma2();
	//saludar_persona(" Pedro");
	return 0;
}

