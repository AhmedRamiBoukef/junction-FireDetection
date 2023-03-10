#include <Servo.h>
Servo myservo;
int pin8 = 8; // buzzer
int pin7 = 7; // relais pompe à eau

int fire =0 ;  // returned from the model  when he will change to one it will pompe water
void setup() { 
    myservo.attach(9);  // SERVO SUR pin D9 
    Serial.begin(9600);
    pinMode(pin8, OUTPUT);
    pinMode(pin7, OUTPUT);
    Serial.begin(9600);
    digitalWrite(pin8, LOW);
    digitalWrite(pin7, LOW);
    myservo.write(170);
}
void loop() {
    myservo.write(10); 
    char fire1;
    delay (1000);
    for ( int balayage = 0 ; balayage <= 180; balayage = balayage + 1 )
    {
        if (Serial.available() > 0) {
        fire1 = Serial.read();
            Serial.print("Received character: ");
            Serial.println(fire1);
        }
        myservo.write(balayage);  
        if (fire1=='1')  
        {
            digitalWrite(pin8, HIGH); // active buzzer
            digitalWrite(pin7, HIGH); // allumage pompe
            for ( int incendie = balayage - 18 ; incendie <= balayage + 15 ; incendie = incendie + 1 ){
                myservo.write(incendie);  
                delay(20);
                if (Serial.available() > 0) {
                    fire1 = Serial.read();
                    Serial.print("Received character: ");
                    Serial.println(fire1);
                    if(fire1=='0'){
                        Serial.println("The fire goes out");
                        break ;
                    }
                }
            }
            digitalWrite(pin7, LOW);
        }
        else {
            digitalWrite(pin8, LOW);
            digitalWrite(pin7, LOW);
        }
    delay (20);
    }
}