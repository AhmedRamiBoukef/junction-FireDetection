#include <Servo.h>

Servo myservo ;
Servo myservo1 ; 
int pin8 = 8; // buzzer
int pin7 = 7; // relais pompe à eau

void setup() { 
myservo.attach(9);  // SERVO SUR pin D9 pour l'axe des X 
myservo1.attach(10) ; // Servo SUR Pin D10 pour l'axe des y 
Serial.begin(9600);
pinMode(pin8, OUTPUT);
pinMode(pin7, OUTPUT);
Serial.begin(9600);
digitalWrite(pin8, LOW);
digitalWrite(pin7, LOW);
myservo.write(170);
}
void loop() {
myservo.write(0); 
  myservo1.write(0); 

  int fire1 ; 
   int angXbegin;
  int angXend ;
   int angYbegin ;
    int angYend ; 
  float angY ; 

if(Serial.available()>0)
{
	String inputString = Serial.readStringUntil('\n');
  	fire1 = inputString.substring(0, 1).toInt(); // 1 s'il ya une incendie 0 sinon 
    angXbegin = inputString.substring(2, 5).toInt(); // angle envoyer par model 
  	angXend = inputString.substring(6, 9).toInt();// angle envoyer par model
    angYbegin = inputString.substring(10, 13).toInt();// angle envoyer par model
    angYend = inputString.substring(14, 17).toInt();// angle envoyer par model
  	angY = (angYbegin+angYend)/2 ; // le center de box d'incendie dans la dimension Y
	Serial.println(fire1) ;
  	Serial.println(angXbegin) ; 
	Serial.println(angXend) ; 
	Serial.println(angYbegin) ; 
	Serial.println(angYend) ;
  	Serial.println(angY) ;


}
if (fire1==1) {
        digitalWrite(pin8, HIGH); // active buzzer
        digitalWrite(pin7, HIGH); // allumage pompe
  		myservo1.write(angY);  
        delay(40);
        for ( int incendie = angXbegin; incendie <= angXend; incendie = incendie + 1 )
        {
          	myservo.write(incendie);
            delay(20);
            if (Serial.available() > 0) {
	 			String str = Serial.readStringUntil('\n');
              	fire1 =str.toInt(); 
                Serial.print("Received character: ");
                Serial.println(fire1);
                if(fire1==0){
                    Serial.println("The fire goes out");
					
                break ;
                }
            }
        }
        digitalWrite(pin7, LOW);
  		digitalWrite(pin8, LOW);

    }
  
}


/***********Note : ******************
les données recu apartir de model en cas de detection d'incendie sont : 
- 1 ou 0 s'il ya une incendie ou pas 
- angXbegin l'angle de début d'incendit dans la demension X
- angXfin l'angle de fin d'incendit dans la demension X
- angYbegin l'angle de début d'incendit dans la demension Y
- angYfin l'angle de fin d'incendit dans la demension Y
-selon ces deux dernier on calcule l'angle angY qui est le center d'incendit dans la demension Y
-les données doivent etre séparé par des virgules 
-les angles doivent etre sur 3 bits
exemple : 1,090,120,050,080 
1:il ya une incendie 
090:angXbegin
120:angXend
050:angYbegin
080:angYend


les données recu apartir de model en cas de detection d'incendie sont : 
-0 qui dit qu'on a pas une incendie ou l'incidie est étinue 

*/









