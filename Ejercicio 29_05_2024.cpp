 
#include <iostream>
#include <cmath>

using namespace std;

void ingrese_3_enteros(){
	
	int a=0;
	int b=0;
	int c=0;
	
	cout<<"ingrese tres numeros enteros porfavor"<<endl;
	cout<<"ingrese valor a: ";cin>>a;
	cout<<"ingrese valor b: ";cin>>b;
	cout<<"ingrese valor c: ";cin>>c;
	
	if(a==b ||b==c||c==a){
		if (a==b){
			cout<<"nuemro "<<a<<" repetido 2 veces"<<endl;
		}
		else if (b==c){
			cout<<"nuemro "<<b<<" repetido 2 veces"<<endl;
		}
		else if (a==b||b==c){
			cout<<"nuemro "<<a<<" repetido 3 veces"<<endl;
		}
		else {
			cout<<"nuemro "<<a<<" repetido 2 veces"<<endl;
		}
	
	}
	else{
		cout<<"no ahi numeros repetidos"<<endl;
	}
}//corregir en casas.....

void switch_(){
	int num;
	cout<<"ingrese un numero del 1 al 7: ";cin>>num;
	switch(num){
		case 1:
			cout<<"lunes"<<endl; break;
		case 2:
			cout<<"martes"<<endl; break;
		case 3:
			cout<<"miercoles"<<endl; break;
		case 4:
			cout<<"jueves"<<endl; break;
		case 5:
			cout<<"viernes"<<endl; break;
		case 6:
			cout<<"sabado"<<endl; break;
		case 7:
			cout<<"domingo"<<endl; break;
		default:
			cout<<"opcion no validad"<<endl; break;
		
	}	
}

void ejercicios(){
	double num,num2;
	char oper;
	cout<<"ingrese primer numero: ";cin>>num;
	cout<<"ingrese segundo nuemro: ";cin>>num2;
	cout<<"ingrese una operacion ( + , - , * ,/): ";cin>>oper;
	switch(oper){
		case '+':
			cout<<"resultado: "<<num+num2<<endl; break;
		case '-':
			cout<<"resultado: "<<num-num2<<endl; break;
		case '*':
			cout<<"resultado: "<<num*num2<<endl; break;
		case '/':
			cout<<"resultado: "<<num/num2<<endl; break;
		default:
			cout<<"opcion no validad"<<endl; break;
	}
}

void dinero(){
	float dol;
	char dinero;
	cout<<" ingrese el valor en dolares: ";cin>>dol;
	cout<<" ingrese el caracter q desea transformar\n a) euro\n b) libra\n c) franco\n d) yen\n e) yuan :\n ";cin>>dinero;
	switch(dinero){
		case 'a':
			cout<<"resultado: "<<dol*0.9226<<" EURO"<<endl; break;
		case 'b':
			cout<<"resultado: "<<dol*0.7851<<" LIBRA ESTERLINA"<<endl; break;
		case 'c':
			cout<<"resultado: "<<dol*0.9123<<" FRANCO SUIZO"<<endl; break;
		case 'd':
			cout<<"resultado: "<<dol*157.3380<<" YEN JAPONES"<<endl; break;
		case 'e':
			cout<<"resultado: "<<dol*7.27<<" yuan chino"<<endl; break;	
		default:
			cout<<"opcion no validad"<<endl; break; 
	
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





int main(){
	ejerfor();
	//dinero();
	return 0;
}
