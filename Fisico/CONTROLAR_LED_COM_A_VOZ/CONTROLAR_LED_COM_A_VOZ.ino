
  
#include <SoftwareSerial.h>
#include "VoiceRecognitionV3.h"

/**        
  Connection
  Arduino    VoiceRecognitionModule
   2   ------->     TX
   3   ------->     RX
*/
VR myVR(2,3);    // 2:RX 3:TX, you can choose your favourite pins.

uint8_t records[7]; // save record
uint8_t buf[64];

int out1 = 10;
int out2 = 11;
int out3 = 12;








#define ARDUINO    (0)
#define LAMPADA   (1) 
#define VENTILADOR   (2)
#define VERMELHO    (3)
#define AMARELO    (4)
#define AZUL (5)

/**
  @brief   Print signature, if the character is invisible, 
           print hexible value instead.
  @param   buf     --> command length
           len     --> number of parameters
*/
void printSignature(uint8_t *buf, int len)
{
  int i;
  for(i=0; i<len; i++){
    if(buf[i]>0x19 && buf[i]<0x7F){
      Serial.write(buf[i]);
    }
    else{
      Serial.print("[");
      Serial.print(buf[i], HEX);
      Serial.print("]");
    }
  }
}

/**
  @brief   Print signature, if the character is invisible, 
           print hexible value instead.
  @param   buf  -->  VR module return value when voice is recognized.
             buf[0]  -->  Group mode(FF: None Group, 0x8n: User, 0x0n:System
             buf[1]  -->  number of record which is recognized. 
             buf[2]  -->  Recognizer index(position) value of the recognized record.
             buf[3]  -->  Signature length
             buf[4]~buf[n] --> Signature
*/
void printVR(uint8_t *buf)
{
  Serial.println("VR Index\tGroup\tRecordNum\tSignature");

  Serial.print(buf[2], DEC);
  Serial.print("\t\t");

  if(buf[0] == 0xFF){
    Serial.print("NONE");
  }
  else if(buf[0]&0x80){
    Serial.print("UG ");
    Serial.print(buf[0]&(~0x80), DEC);
  }
  else{
    Serial.print("SG ");
    Serial.print(buf[0], DEC);
  }
  Serial.print("\t");

  Serial.print(buf[1], DEC);
  Serial.print("\t\t");
  if(buf[3]>0){
    printSignature(buf+4, buf[3]);
  }
  else{
    Serial.print("NONE");
  }
  Serial.println("\r\n");
}

void setup()
{
  /** initialize */
  myVR.begin(9600);
  
  Serial.begin(115200);
  Serial.println("Elechouse Voice Recognition V3 Module\r\nControl LED sample");
  

  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
    
  if(myVR.clear() == 0){
    Serial.println("Recognizer cleared.");
  }else{
    Serial.println("Not find VoiceRecognitionModule.");
    Serial.println("Please check connection and restart Arduino.");
    while(1);
  }
  
  if(myVR.load((uint8_t)ARDUINO) >= 0){
    Serial.println("onRecord loaded");
  }
  if(myVR.load((uint8_t)LAMPADA) >= 0){
    Serial.println("onRecord loaded");
  }
  if(myVR.load((uint8_t)VENTILADOR) >= 0){
    Serial.println("onRecord loaded");
  }
  if(myVR.load((uint8_t)VERMELHO) >= 0){
    Serial.println("onRecord loaded");
  }
  if(myVR.load((uint8_t)AMARELO) >= 0){
    Serial.println("onRecord loaded");
  }
  if(myVR.load((uint8_t)AZUL) >= 0){
    Serial.println("offRecord loaded");
  }
}

void loop()
{
  int ret;
  ret = myVR.recognize(buf, 50);
  if(ret>0){
    switch(buf[1]){
      case ARDUINO:
        /** turn on LED */
digitalWrite(10,HIGH); 
delay(400);
digitalWrite(10,LOW); 

 
 
        break;
      case LAMPADA:
        /** turn off LED*/
if(digitalRead(5)==LOW){
digitalWrite(11,HIGH); 
delay(400); 
digitalWrite(11,LOW);}
if(digitalRead(5)==HIGH){
digitalWrite(12,HIGH); 
delay(400); 
digitalWrite(12,LOW);  
}
     
digitalWrite(5, !digitalRead(5));

        break;

        case VENTILADOR:
        /** turn off LED*/
if(digitalRead(6)==LOW){
digitalWrite(11,HIGH); 
delay(400); 
digitalWrite(11,LOW);}
if(digitalRead(6)==HIGH){
digitalWrite(12,HIGH); 
delay(400); 
digitalWrite(12,LOW);  
}      
  digitalWrite(6, !digitalRead(6));
        break;

case VERMELHO:
        /** turn off LED*/
if(digitalRead(7)==LOW){
digitalWrite(11,HIGH); 
delay(400); 
digitalWrite(11,LOW);}
if(digitalRead(7)==HIGH){
digitalWrite(12,HIGH); 
delay(400); 
digitalWrite(12,LOW);  
}          

 digitalWrite(7, !digitalRead(7));
        break;


        case AMARELO:
        /** turn off LED*/
if(digitalRead(8)==LOW){
digitalWrite(11,HIGH); 
delay(400); 
digitalWrite(11,LOW);}
if(digitalRead(8)==HIGH){
digitalWrite(12,HIGH); 
delay(400); 
digitalWrite(12,LOW);  
}
 digitalWrite(8, !digitalRead(8));
        break;



        case AZUL:
        /** turn off LED*/
if(digitalRead(9)==LOW){
digitalWrite(11,HIGH); 
delay(400); 
digitalWrite(11,LOW);}
if(digitalRead(9)==HIGH){
digitalWrite(12,HIGH); 
delay(400); 
digitalWrite(12,LOW);  
}  
 digitalWrite(9, !digitalRead(9));
        break;
      default:
        Serial.println("Record function undefined");
        break;
    }

    
    /** voice recognized */
    printVR(buf);
  }
}
