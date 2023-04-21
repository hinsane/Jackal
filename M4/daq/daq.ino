const int samplingRate = 1 / 1.05e5;  // Sampling rate = 1/frequency
const int baudRate = 9600;            // baud rate
double micData = 0;
#define mic A0
const int samplingTime = 10;  // Sampling time in seconds

String command_1;
String command_2;
String report;


void setup() {

  pinMode(mic, INPUT);

  Serial.begin(baudRate);

  _init_();

  startCode();
}



void loop() {

  listen();
  delay(samplingRate);
}

// Connecting M4 to Jackal via serial port

void connect() {

  Serial.println("Attempting to connect\n");

  report = Serial.readStringUntil('\n');

  while (report.equals("Connection Successful!") == false) {
    report = Serial.readStringUntil('\n');
  }
}

void _init_() {

  command_1 = Serial.readStringUntil('\n');

  while (command_1.equals("Initiate") == false) {
    command_1 = Serial.readStringUntil('\n');
  }
  connect();
}

void startCode() {

  Serial.println("Starting program in 2 seconds\n");

  command_2 = Serial.readStringUntil('\n');
  while (command_2.equals("startCode") == false) {
    command_2 = Serial.readStringUntil('\n');
  }
  delay(2000);
  loop();
}

void listen() {
  micData = analogRead(mic);
  Serial.println(micData);
}