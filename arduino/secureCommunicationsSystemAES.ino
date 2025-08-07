void setup() {
	Serial.begin(9600);
	while (!Serial) {} //waits for serial port to connect
	Serial.println("AES Arduino Receiver Ready");
}

void loop(){
	if (Serial.available()) {
		String encryptedMessage = Serial.readStringUntil('\n');
		Serial.print("Recieved Encrypted Message: ");
		Serial.println(encryptedMessage);
	}
}
