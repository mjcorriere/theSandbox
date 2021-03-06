
//Movement status
int going;
int strafeLeft, strafeRight;

float theta;

//Ball radius
int r;

//Radians per pixel

float c;

//Position, velocity, and acceleration of Ball
PVector pos, vel, acl;
PVector mPos;

//Change in mouse coordinates
float delM;

//Normalized look direction
PVector nLook;

//Normalized perpendicular (CCW) look direction
PVector pLook;

//Magnitude of constant acceleration
float a;

//Magnitude of velocity
float v;

//Friction coefficient
float f;

void setup() {
  
  size(640, 480);
  background(0);
  stroke(255);
  strokeWeight(4);
  smooth();
  
  noCursor();
  
  //Initialize position, vel, acceleration
  pos = new PVector(width/2, height/2);
  vel = new PVector(0, 0);
  acl = new PVector(0, 0);
  
  mPos = new PVector(mouseX, mouseY);
  
  nLook = new PVector(0,0);
  pLook = new PVector(0,0);  
  
  delM = 0;
  
  a = .25;
  f = .98;
  
  v = 2.5;
  
  r = 50;
  
  going = 0;
  strafeLeft = 0;
  strafeRight = 0;
  
  c = PI / 120;
  theta = 0;
   
}

void draw() {
  
  background(0);
  
  mPos.set( mouseX, mouseY, 0);
  delM = mouseX - pmouseX;

  theta += c * delM;
  
  nLook.set( cos(theta), sin(theta), 0);

//  nLook.set( mPos.x - pos.x, mPos.y - pos.y, 0);
//  nLook.normalize();
  
  pLook.set(nLook.y, -nLook.x, 0);
 
  if (going == 1 || strafeLeft == 1 || strafeRight == 1) go();

  moveIt();
  colDetect();
  
  stroke(255);
  ellipse(pos.x, pos.y, r/2, r/2);
//  ellipse(mPos.x, mPos.y, 5, 5);
  
  stroke(200, 0, 0);
  line(pos.x, pos.y, pos.x + nLook.x * .75*r, pos.y + nLook.y * .75*r);
  stroke(255);
  line(pos.x, pos.y, pos.x + pLook.x * .5*r, pos.y + pLook.y * .5*r);  
  line(pos.x, pos.y, pos.x - pLook.x * .5*r, pos.y - pLook.y * .5*r);  

  if (going == 1) {

    stroke(255, 0, 0);
//    line(mPos.x, mPos.y, pos.x, pos.y);
    
  }
      
}

void keyPressed() {
  
  if (key == 'W' || key == 'w') going = 1;
  if (key == 'A' || key == 'a') strafeLeft = 1;
  if (key == 'D' || key == 'd') strafeRight = 1;  
  
}

void keyReleased() {
  
  if (key == 'W' || key == 'w') going = 0;
  if (key == 'A' || key == 'a') strafeLeft = 0;  
  if (key == 'D' || key == 'd') strafeRight = 0;    
  
}

void go() {
  
  PVector dst;
  dst = new PVector(0,0);
  
//  dst.set(pos.x + delM.x, pos.y + delM.y, 0);
//  dst.set(mPos.x - pos.x, mPos.y - pos.y, 0);
//  dst.normalize();
  

  if (strafeLeft == 1) {

    if (going == 1) {
      dst.set (nLook.x + nLook.y, nLook.y - nLook.x, 0);
      dst.mult(0.707106781);
    }      
    else
      dst.set (nLook.y, -nLook.x, 0);
      
  }
    
  else if (strafeRight == 1) {
    
    if (going == 1) {
      dst.set (nLook.x - nLook.y, nLook.x + nLook.y, 0);
      dst.mult(0.707106781);
    }
    else
      dst.set (-nLook.y, nLook.x, 0);
      
  }
  
    else
      dst.set (nLook.x, nLook.y, 0);
  
  dst.mult(v);

//  dst.mult(a);
  
//  acl.set(dst);
  vel.set(dst);  

}

void moveIt() {
  
  vel.mult(f);  
  pos.add(vel);  
  
}

void colDetect() {
  
  if ((pos.x - r/2 < 0) || ((pos.x + r/2) > width))
    pos.x -= vel.x;
    
  if ((pos.y - r/2 < 0) || ((pos.y + r/2) > height))
    pos.y -= vel.y;    
  
}
