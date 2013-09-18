
PImage treeguy;
PImage tree, treetop;
PImage unicorn;
PImage cloud, cloudface;

int tx, ty, uniX, uniY;

boolean isTreeGuyJumping, goingDown;

void setup() {
  
  size(640, 480);
  smooth();
  
  treeguy = loadImage("treeguy.png");
  unicorn = loadImage("hornyunicorn.png");
  tree = loadImage("tree_resize.png");
  cloud = loadImage("cloud.png");
  cloudface = loadImage("cloudface.png");
  treetop = loadImage("treetop.png");
  
  uniX = width - 75 - unicorn.width;
  uniY = height - 40 - unicorn.height;
  tx = 30;
  ty = height - 40 - treeguy.height;
  
  isTreeGuyJumping = false;
  goingDown = false;
  
}

void draw() {
  
  background(0, 0, 215);
  fill(0, 150, 60);
  rect(0, height - 75, width, height);
  
  if (isTreeGuyJumping) {
    jumpTreeGuy();        
  }
  
  image(cloud, (frameCount/3 + 85) % (width + cloud.width) - cloud.width, 100);  
  image(cloudface, (frameCount / 2) % (width + cloudface.width) - cloudface.width, 15);
  image(tree, (width - tree.width)/2, (height - tree.height)/2);
  image(unicorn, uniX, uniY);
  image(treeguy, tx, ty);  
  image(treetop, (width - treetop.width)/2, (height - treetop.height)/2);
 
}

void keyPressed() {
  
  if (key == CODED) {
    
    if (keyCode == LEFT)
      uniX = uniX - 10;
    else if (keyCode == RIGHT)
      uniX = uniX + 10;
      
    if (uniX + unicorn.width/2 > 289 && uniX + unicorn.width/2 < 355) {
      if (keyCode == UP)
        uniY = uniY - 20; 
     
      if (keyCode == DOWN)
        uniY = uniY + 20;      
      
    }
  
  } //endif key == CODED
  
  if (key == 'd' || key == 'D')
    tx = tx + 10;
    else if (key == 'a' || key == 'A')
      tx = tx - 10; 
      
  if (key == 'w' || key == 'W')
    isTreeGuyJumping = true;
    
    
}

void jumpTreeGuy() {
  
  if (ty > height - 40 - treeguy.height) {
    ty = height - 40 - treeguy.height;
    isTreeGuyJumping = false;
    goingDown = false;
    return;
  }
  
  else {

    if (ty < height - 40 - treeguy.height - 60)
      goingDown = true;

    if (!goingDown)
      ty -= 5;
    else {
      ty += 5;
    }
    
  } 
  
}
  




