class Ball {
  
  float x, y;
  float Vx, Vy;
  
  float accel, friction;

  int r, d;
  color clr, fClr;
  
  int bFlash;

  Ball(float inpX, float inpY, int inpR, color inpColor) {
    
    x = inpX;
    y = inpY;
    
    accel = .25;
    friction = .98;
    
    r = inpR;
    d = 2*r;
    
    clr = inpColor;
    fClr = color(120, 192, 60);
    
    bFlash = 0;
    
  }
  
  void checkWall() {
    
    if (x-r < 0)           { x = r; Vx = 0; }
    if (y-r < 0)           { y = r; Vy = 0; }
    if ((x+r) > width)     { x = width - r; Vx = 0; }    
    if ((y+r) > height)    { y = height - r; Vy = 0; }  
 
  }   
    
  boolean checkCol(Ball obj) {
    
    float dist2;

    float ox = obj.getX();
    float oy = obj.getY();
    float or = obj.getR();

    dist2 = sq(oy - y) + sq(ox - x);
    
    if (dist2 <= sq(or + r)) return true;
      else return false;
    
  }
  

  float getX() {
    
    return x;
    
  }
  
  float getY() {
    
    return y;
    
  }
  
  int getR() {
    
    return r;
    
  }

  void setX(float xPos) {
    
    x = xPos;
    
  }
  
  void setY(float yPos) {
    
    y = yPos;
    
  }

  void setPos(float xPos, float yPos) {
    
    x = xPos;
    y = yPos;

  }
  
  float getVx() {
    
    return Vx;
    
  }
  
  float getVy() {
    
    return Vy;
    
  }

  void setVx(float xVel) {
    
    Vx = xVel;
    
  }
  
  void setVy(float yVel) {
    
    Vy = yVel;
    
  }

  void setVel(float xVel, float yVel) {
    
    x = xVel;
    y = yVel;

  }

  void moveIt(int[] dir) {
    
    //dir
    //0 = Up
    //1 = Down
    //2 = Left
    //3 = Right
    
    if (dir[0] == 1)  Vy -= accel;
    if (dir[1] == 1)  Vy += accel;
    if (dir[2] == 1)  Vx -= accel;
    if (dir[3] == 1)  Vx += accel;
    
  }
  
  void update() {
                
    Vx *= friction;
    Vy *= friction;    
    
    x += Vx;
    y += Vy;
    
  }
  
  void flash(int fOn) {
    
    if (fOn == 1) bFlash = 1;
      else bFlash = 0;   

  }

  void display() {
    
    if (bFlash == 1) fill(fClr);
      else fill(clr);
    
    strokeWeight(3);
    ellipse(x, y, d, d);
    
  }
  
}
