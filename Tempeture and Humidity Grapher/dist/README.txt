Temperature and Humidity Grapher
Description:
The idea is simple, sensor.ino is the arduino script is mounted directly on the board. This script read data from two sensors (Temperature and Humidity) and then sends this data in 30m intervals through serial Communication via usb cable. Then scriptDataInsertion.py reads the data sent from the aruduino in the computers serial port and stores it in a sqlite database. Finally Projecto_Final1.java gets the data from the database and then graphs it in a line graph that has two lines, one for temperature the other for humidity.

Whats included:
-ScriptDataInsertion.py(python script for reading serial data from arduino, parsing it , and storing it in a database.
-ProyectoFinal1.db (database where humidity and temperature is stored)
-ProyectoFinal.jar (java file that pulls data out of the database and graphs it)
- lanzador.bat (batch file that executes both scriptdatainsertion.py and ProyectoFinal.jar at the same time)
