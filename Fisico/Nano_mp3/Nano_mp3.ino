
//Inclusão das bibliotecas
#include "Arduino.h"
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"


//Inicia a serial por software nos pinos 10 e 11
SoftwareSerial mySoftwareSerial(10, 11); // RX, TX

//Objetos 
DFRobotDFPlayerMini myDFPlayer;

int ent1 = 2;
int ent2 = 3;
int ent3 = 4;
 
 void setup ( ) {
  pinMode(ent1,INPUT);
  pinMode(ent2,INPUT); 
  pinMode(ent3,INPUT);
  //Comunicacao serial com o modulo
    mySoftwareSerial.begin(9600);
  //Inicializa a serial do Arduino
  Serial.begin(115200);

  //cartao SD foi encontrado
  Serial.println();
  Serial.println(F("DFRobot DFPlayer Mini"));
  Serial.println(F("Inicializando modulo DFPlayer... (3~5 segundos)"));
  if (!myDFPlayer.begin(mySoftwareSerial))
  {
    Serial.println(F("Nao inicializado:"));
    Serial.println(F("1.Cheque as conexoes do DFPlayer Mini"));
    Serial.println(F("2.Insira um cartao SD"));
    while (true);
  }
  Serial.println();
  Serial.println(F("Modulo DFPlayer Mini inicializado!"));

  //Definicoes iniciais
  myDFPlayer.setTimeOut(500); //Timeout serial 500ms
  myDFPlayer.volume(29); //Volume 21
  myDFPlayer.EQ(0); //Equalizacao normal

  //Mostra o quantidade de arquivos no cartão SD
  Serial.println();
  Serial.print("Numero de arquivos no cartao SD: ");
  Serial.println(myDFPlayer.readFileCounts(DFPLAYER_DEVICE_SD));

 } 

 
void loop() {
    ent1=digitalRead(2);
    if(ent1==HIGH){
    myDFPlayer.play(01);
    Serial.println("Arquivo 1");
    delay(3000);}

    ent2=digitalRead(3);
    if(ent2==HIGH){
    myDFPlayer.play(02);
    Serial.println("Arquivo 2");
    delay(3000);}

    ent3=digitalRead(4);
    if(ent3==HIGH){
    myDFPlayer.play(03);
    Serial.println("Arquivo 3");
    delay(3000);}
  

}
