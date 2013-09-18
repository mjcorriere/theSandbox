Ship theShip;

void setup() {
  
  size(640, 480);
  
  theShip = new Ship(width/2, height/2);
  
  
}

void draw() {
  
  background(0);
  
  theShip.update();
  theShip.display();  
  
}

void keyPressed() {
  
  if (key == 'w' || key == 'W')
    theShip.setUpState(1);
  if (key == 's' || key == 'S')
    theShip.setDownState(1);
  if (key == 'd' || key == 'D')
    theShip.setRightState(1);  
  if (key == 'a' || key == 'A')
    theShip.setLeftState(1); 
  
}

void keyReleased() {
  
  if (key == 'w' || key == 'W')
    theShip.setUpState(0);
  if (key == 's' || key == 'S')
    theShip.setDownState(0);
  if (key == 'd' || key == 'D')
    theShip.setRightState(0);  
  if (key == 'a' || key == 'A')
    theShip.setLeftState(0); 
  
}
