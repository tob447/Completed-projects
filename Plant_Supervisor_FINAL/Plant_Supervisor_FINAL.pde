import processing.serial.*;
Serial myPort; // The serial port
PImage img,img1,img2;
PFont font;

int total_Temp=0;
int total_Light=0;
int total_Humidity=0;

int light=0;
int temp=0;
int humidity=0;

void setup()
{
      println(Serial.list());

    // Setup which serial port to use.
    // This line might change for different computers.
    
    
    //myPort = new Serial(this, Serial.list()[0], 9600);
    
    System.setProperty("gnu.io.rxtxSerialPorts", "/dev/ttyACMO",9600);
    myPort=new Serial(this,"/dev/ttyACMO");
    
    
    img2=loadImage("leaves.jpg");
  img = loadImage("lightbulb.jpg");
  img1 =loadImage("thermo.jpg");
   
  

  size(800,600);
   background(img2);
  
 
  
   rectMode(CENTER);
 stroke(0);
 fill(220);

// rect(width/2+100,height/2+25, 450,100);
  //rect(width/2+100,150, 450,100);
  //rect(width/2+100,500,450,100);

 // image(img, 0, 0, width/2, height/2);
 
 image(img1,50,225);
 textSize(30);
 fill(0);
 text("Light Percentage",370,80);
 textSize(30);
 fill(0);
 text("Temperature",390,265);
 textSize(30);
 fill(0);
 text("Humidity",420,430);
 
  
}

void draw() {

  
}


 void serialEvent (Serial myPort) {
    // read the string from the serial port.
    String inString = myPort.readStringUntil('\n');

    if (inString != null) {
    // trim off any whitespace:
    inString = trim(inString);
    int space = inString.indexOf(" ");
    String option = inString.substring(0,space);
    String value = inString.substring(space, inString.length());
    
    if(option.equals("light")){
  
    
    value= trim(value);
   
    light = int(value);
    light= light*100/1000;
     
     
   rectMode(CENTER);
   stroke(0);
   fill(220);
 
//rect(width/2+100,height/2+100, 500,150);
  rect(width/2+100,150, 450,100);

     
    font = loadFont("Arial-BoldMT-48.vlw");
    textFont(font, 48);
    fill(0);
     text(light + "%",width/2+40,160);    
      total_Light=total_Light+light;
    }
    
    else if(option.equals("temp")){
      
    
    value= trim(value);
   
    temp = int(value);
    
     
   rectMode(CENTER);
   stroke(0);
   fill(220);
 
    rect(width/2+100,height/2+25, 450,100);
     
    font = loadFont("Arial-BoldMT-48.vlw");
    textFont(font, 48);
    fill(0);
    text(temp + "C°",450,350);
    total_Temp=total_Temp+temp;
      
    
 }
 
 
     else if(option.equals("humidity")){
      
   
    value= trim(value);
   
    humidity = int(value);
    
     
   rectMode(CENTER);
   stroke(0);
   fill(220);
   rect(width/2+100,500,450,100);
   //rect(width/2+100,150, 500,150);

     
    font = loadFont("Arial-BoldMT-48.vlw");
    textFont(font, 48);
    fill(0);
    text(humidity + "%",450,510);
    total_Humidity=total_Humidity+humidity;
    
      
    
 }
 
    }
    
    if(minute()==56)
    {
      int Average_Light=total_Light/60;
      int Average_Temp=total_Temp/60;
      int Average_Humidity=total_Humidity/60;
      
      println(Average_Light);
      println(Average_Temp);
      println(Average_Humidity);
      
      String Averages=str(Average_Light)+" "+str(Average_Temp)+" "+str(Average_Humidity);
      String[]  Average_List =split(Averages, " ");
      
      saveStrings("sensorsData2.txt", Average_List);
      

      
    }
    
    
 }
