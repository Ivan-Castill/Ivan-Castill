#include <iostream>

using namespace std;

void bucle_for(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=5; j<=num;j+=5){
		cout<< "N.-"<<j<<" hi usuario"<<endl;
	}
	
}
void ejerfor(){
	int j=0;
	cout<<" cuantas lineas desea mostrar"<<endl;
	cin>>j; 
	for(int k=1;k<=j;k++){
		cout<<"N.-"<<k<<" TIRATE DE LA CARRERA"<<endl;
	}
}

void ejercicio(){
	int j=0;
	cout<<" Que tabla de multiplicar desea(escriba el numero):"<<endl;
	cin>>j; 
	for(int k=1;k<=10;k++){
		cout<<"5*"<<k<<"="<<5*k<<endl;
	}
	//for(int j++;j<= num)
	
}

void bucle_for_I(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=num; j>=0;j--){
		cout<< "N.-"<<j<<" hi usuario"<<endl;
	}
}

void bucle_for_anidado(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=1; j<=num;j+=1){
		cout<<"*";
		//bucle anidado
		for(int j=1; j<=num;j+=1){
			cout<<"*";	
		}
	cout<<endl;
	}
	
}

void triangulo(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=1; j<=num;++j){
		cout<<"\n*";
		//bucle anidado
		for(int i=2; i<=j;++i){
			cout<<"*";	
		}
	cout<<endl;
	}
	
}

void triangulo_I(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=num; j>=1;--j){
		cout<<"\n*";
		//bucle anidado
		for(int i=2; i<=j;++i){
			cout<<"*";	
		}
	cout<<endl;
	}
	
}

void triangulo_Completo(){
	int num=0;
	cout<<" Ingrese un numero por teclado"<<endl;
	cin>>num;
	
	for(int j=1; j<=num;++j){
		//bucle anidado
	for(int i=1; i<=num-j;++i){
		cout<<" ";
	}
	for(int i=1; i<=2*j-1;++i){
		cout<<"*";
	}
	cout<<endl;
	}
	
}

int main(){
	triangulo_Completo();
	//triangulo_I();
	//triangulo();
	//bucle_for_anidado();
	//ejercicio();
	//bucle_for_I();
	//bucle_for();
	return 0;
}
