 char key = 'k';

void setup() {
  Serial.begin(9600);
  delay(1000);
  Serial.println("Ready to recieve encrypted messages...");

}

void loop() {
 if (Serial.available() > 0) {
    String encryptedMessage = Serial.readStringUntil('\n'); //reads full message
    String decryptedMessage = xorDecrypt(encryptedMessage, key);
    
    Serial.println ("Encrypted " + encryptedMessage);
    Serial.println("Decrypted " + decryptedMessage);
 }

}

String xorDecrypt(String input, char key) {
  String output = "";

  for (int i = 0; i < input.length(); i++) {
    output += char(input[i] ^ key); //this XOR's each character
  }

  return output;
}