
//------------------------------------------------------------------------------------
//                         Fixed Wing Flight Controller Code V1.0
//------------------------------------------------------------------------------------
/*
 * Fixed Wing Flight Controller Software uses a Arduino Nicla Sense ME. Used to take commands from a Raspberry Pi via i2c
 */
// Matthew Haywood

#include "Arduino_BHY2.h"
#include <Wire.h>
#include <Servo.h>
#include <pid_loop.h>
#include <splitString.h>

Servo Motor1; // Aileron Left/Right
Servo Motor2; // Elevator
Servo Motor3; // Rudder
Servo Motor4; // Throttle (ESC brushless motor, not actually a servo motor) probably won't be used to start with either.

float motor1Angle;
float motor2Angle;
float motor3Angle;
float throttleValue = 1100;

float roll_pid_output;
float pitch_pid_output;
float heading_pid_output;

float desired_roll_value;
float desired_pitch_value;

int MIN = 1100;
int MAX = 1900;

Sensor device_orientation(SENSOR_ID_DEVICE_ORI);
SensorOrientation orientation(SENSOR_ID_ORI);
Sensor pressure(SENSOR_ID_BARO);

PID_LOOP ROLL_PID(2.0, 0, 0.4);
PID_LOOP PITCH_PID(2.0, 0, 0);
PID_LOOP HEADING_PID(0.5, 0, 0);

void setup() {
  // put your setup code here, to run once:
  Motor1.attach(9);
  Motor2.attach(8);
  Motor3.attach(7);
  Motor4.attach(6);

  //Arm motor 4 by running calibration

  Motor4.writeMicroseconds(1500);
  delay(3000);
  Motor4.writeMicroseconds(1100);
  
  BHY2.begin();
  pressure.begin();
  orientation.begin();
  delay(1000);
  BHY2.update();

  Serial.begin(115200);

  Wire.begin(8); // set up i2c connection with raspberry pi
  Wire.onReceive(receiveEvent);
  Wire.onRequest(sendData);

  Serial.println("Starting up");

  desired_roll_value = 0;
  desired_pitch_value = 15;
  
}

void sendData(){

Wire.write(0);
  
}

void receiveEvent(int howMany){

  char commandsChar[] = {'.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'};

  int index = 0;
  
  while(1 < Wire.available()){
      
      char c = Wire.read();
      
      if(c != ' '){

        commandsChar[index] = c;

        index = index + 1;
        
        } else if (c == ' '){
        
      }
      
    }

    if(commandsChar[1] == 'R'){

      Serial.println("change pid desired");
      char rollValueSign = commandsChar[2];
      char pitchValueSign = commandsChar[6];

      desired_roll_value = 10*(commandsChar[3] - '0') + commandsChar[4] - '0';

      desired_pitch_value = 10*(commandsChar[7] - '0') + commandsChar[8] - '0';
      
      if(rollValueSign == '-'){
        desired_roll_value = - desired_roll_value;
      }

      if(pitchValueSign == '-'){
        desired_pitch_value = - desired_pitch_value;
      }
      
      throttleValue = 1000*(commandsChar[10] - '0') + 100*(commandsChar[11] - '0') + 10*(commandsChar[12] - '0') + commandsChar[13] - '0';

      //R10P30T1400

      Serial.println(desired_roll_value);
      Serial.println(desired_pitch_value);
      Serial.println(throttleValue);

 
      //Change desired angles and throttle here!
      
    } else if(commandsChar[0] == 'A') {

      //Raspberry Pi is Requesting Altitude so send back altitude

      Serial.println("Send Altitude");
  
      Serial.println(String(pressure.value()));
      
    }
  
}

void loop() {
  // put your main code here, to run repeatedly:

  BHY2.update();

  roll_pid_output = ROLL_PID.compute_loop(desired_roll_value, orientation.roll());
  pitch_pid_output = PITCH_PID.compute_loop(desired_pitch_value, orientation.pitch());
  heading_pid_output = HEADING_PID.compute_loop(0, orientation.heading());

  motor1Angle = map(roll_pid_output, -90*ROLL_PID.getPTerm(), 90*ROLL_PID.getPTerm(), 0, 180);
  motor2Angle = map(pitch_pid_output, -90*PITCH_PID.getPTerm(), 90*PITCH_PID.getPTerm(), 0, 180);
  motor3Angle = map(heading_pid_output, -90*PITCH_PID.getPTerm(), 90*PITCH_PID.getPTerm(), 0, 180);

  Motor1.write(int(motor1Angle));
  Motor2.write(int(180-motor2Angle));
  Motor3.write(int(motor3Angle));
  Motor4.writeMicroseconds(throttleValue);
  
}
