#define PIN_LED 13

void setup(){
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(115200);
  while(!Serial){
    ;
  }
  Serial.println("Hello world");
  int count = 0;
  int toggle = 0;
  digitalWrite(PIN_LED, toggle);
}

void loop(){
  int count =0,toggle=0;
  Serial.println(++count);
  toggle = toggle_state(toggle);
  digitalWrite(PIN_LED, toggle);
  delay(1000);
}

int toggle_state(int toggle){
  if(toggle==0) return 1;
  else return 0;
}