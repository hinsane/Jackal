const int samplingRate = 1 / 1.05e5;
const int baudRate = 115200;
double micData = 0;
const int mic = A0;
const int samplingTime = 10;  // Sampling time in seconds

String command_1;
String command_2;
String report;


void setup() {

  pinMode(mic, INPUT);

  Serial.begin(baudRate);

  command_1 = Serial.readStringUntil('\n');

  if (command_1.equals("Initiate") == false) {
    while(1){}
  }
  else if(command_1.equals("Initiate") == true){
    connect();
  }
  command_2 = Serial.readStringUntil('\n');

  if (command_2.equals("startCode")) {
    loop();
  } else {
    disconnect();
  }
}


void loop() {

  micData = analogRead(mic);
  Serial.println(micData);
  delay(samplingRate);
}



void connect() {
  for (int i = 0; i < 3; i++) {

    Serial.println("Attempting to connect");
    delay(100);

    report = Serial.readStringUntil('\n');
    delay(1000);
  }
}

void disconnect() {
  if (report.equals("Connection Successful!")) {
    Serial.println("Starting program in 2 seconds");
    delay(10000);
  } else {
    Serial.println("Connection failed :(");
    delay(100);
    Serial.println("Ending program in 2 seconds");
    delay(2000);
  }
}