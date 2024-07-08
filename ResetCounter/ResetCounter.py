int yaxis, xaxis, switch2, joyY, joyX;

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  yaxis = analogRead(A1);
  xaxis = analogRead(A0);
  switch2 = analogRead(A2);

  joyX = map(xaxis, 0, 1023, -1, 1); 
  joyY = map(yaxis, 0, 1023, -1, 1); 
  
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);

  if (joyY < 0) digitalWrite(9, HIGH);
  else if (joyY > 0) digitalWrite(10, HIGH);
  if (joyX < 0) digitalWrite(11, HIGH);
  else if (joyX > 0) digitalWrite(12, HIGH);

  delay(100);
}
