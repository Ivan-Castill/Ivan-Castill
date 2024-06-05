#include <iostream>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
using namespace std;
void generacion_de_numeros_aleatorios(){
	srand(time(0));
	double aleatorio=(double)rand()/RAND_MAX;
	cout <<"Numero aleatorio entre 0 y 1: "<<aleatorio<<endl;
}

void inicializar_generador_aleatorio(){
	srand(time(0));
}
void lanzamiento_moneda(){
	double aleatorio=(double)rand()/RAND_MAX;
	if (aleatorio<0.5){
	cout<<"CARA"<<endl;
	}
	else{
		cout<<"SELLO"<<endl;	
	} 
}

void inicializar_generador_de_tragaperras(){
	srand(time(0));
}
char lanzamiento_de_valores(){
	char opcion;
	double aleatorio=(double)rand()/RAND_MAX;
	if(aleatorio<0.33){
	//	cout<<"-----"<<endl;
	//	cout<<"| A |"<<endl;
	//	cout<<"-----"<<endl;
		opcion='A';
	}
	else if (aleatorio>0.33 && aleatorio>0.66){
	//	cout<<"-----"<<endl;
	//	cout<<"| B |"<<endl;
	//	cout<<"-----"<<endl;
		opcion='B';
	}
	else{
	//	cout<<"-----"<<endl;
	//	cout<<"| C |"<<endl;
	//	cout<<"-----"<<endl;
		opcion='C';
	}
	return opcion;
}

void inicializar_generador_de_dados(){
	srand(time(0));
}
int lanzamiento_de_dados(){
	int num;
	double aleatorio=(double)rand()/RAND_MAX;
	if(aleatorio<0.17){
		num=1;
	}
	else if (aleatorio>0.17 && aleatorio>0.34){
		num=2;
	}
	else if (aleatorio>0.34 && aleatorio>0.51){
		num=3;
	}
	else if (aleatorio>0.51 && aleatorio>0.68){
		num=4;
	}
	else if (aleatorio>0.68 && aleatorio>0.85){
		num=5;
	}
	else{
		num=6;
	}
	return num;
}



int main(){
	inicializar_generador_de_dados();
	for(int i=1;i<=20;i++){
		int vari1=lanzamiento_de_dados();
		int vari2=lanzamiento_de_dados();
		int vari3=lanzamiento_de_dados();
		cout<<vari1<<"\t"<<vari2<<"\t"<<vari3<<endl;
	}
	
	/*
	inicializar_generador_de_tragaperras();
	char variable1=lanzamiento_de_valores();
	//scanf()
	char variable2=lanzamiento_de_valores();
	char variable3=lanzamiento_de_valores();
//	cout<<"| "<<variable1<<" |"<<"\t"<<"| "<<variable2<<" |"<<"\t"<<"| "<<variable3<<" |"<<endl;
	printf("")
	if(variable1 == variable2 and variable2 == variable3){
		cout<<"GANO"<<endl;
	}else cout<<"PERDIO"<<endl;
	
	//inicializar_generador_aleatorio();
	//for(int i=1;i<=5;i++){
	//	lanzamiento_moneda();
	//}
	//generacion_de_numeros_aleatorios();
	return 0;
	*/
}


