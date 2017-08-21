#include "DHT.h"
#include <TimeLib.h>
#define DHTPIN 7
#define DHTTYPE DHT11
DHT dht (DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  setTime(16,0,0,8,11,2016);
}

void loop() {
  time_t x= now();
  String h=(String)dht.readHumidity();
  String t=(String)dht.readTemperature();
  if(minute(x)==30 && second(x)==0 )
  {
    Serial.println(h+" "+t);                         
  }
}
