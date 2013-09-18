
Ball myBall, theBall;

int[] movState = new int[4];

void setup() {
  
  size(640, 480);
  
  myBall  = new Ball(width/2, height/2, 35, color(200, 20, 20));
  theBall = new Ball(width/3, height/3, 20, color(255, 255, 255));

  background(0);
  stroke(255);
  smooth();
  
}
  
void draw() {
   
  background(148, 158, 123);

  myBall.moveIt(movState);
  
  if  (myBall.checkCol(theBall)) { 
     
    myBall.flash(1);
    
    float delX, delY;
    
    delX = theBall.x - myBall.x;
    delY = theBall.y - myBall.y;    
    
    float angle = atan2(delY, delX);
    
    //acceleration will be treated as a function
    //of their overlap. We pretend when overlapping, the masses
    //act on each other like springs. F = -kx
    
    float ax, ay;

    ax = delX * .03;
    ay = delY * .03;
    
    theBall.Vx += ax;
    theBall.Vy += ay;    
    
    myBall.Vx -= ax;
    myBall.Vy -= ay;    

    //original collision method    
    
//    theBall.Vx = 1.5 * myBall.Vx;
//    theBall.Vy = 1.5 * myBall.Vy;    
    
  }  else myBall.flash(0);
    
  myBall.checkWall();
  theBall.checkWall();
  
  myBall.update();
  theBall.update();

  myBall.display();
  theBall.display();
  
}

void keyPressed() {
  
  if (key == 'W' || key == 'w') movState[0] = 1;
  if (key == 'S' || key == 's') movState[1] = 1;
  if (key == 'A' || key == 'a') movState[2] = 1;
  if (key == 'D' || key == 'd') movState[3] = 1;
  
  if (key == 'J' || key == 'j') myBall.kicking();
  
}

void keyReleased() {
  
  if (key == 'W' || key == 'w') movState[0] = 0;
  if (key == 'S' || key == 's') movState[1] = 0;
  if (key == 'A' || key == 'a') movState[2] = 0;
  if (key == 'D' || key == 'd') movState[3] = 0;
  
  if (key == 'J' || key == 'j') myBall.stopKicking();
  
}
    
  

