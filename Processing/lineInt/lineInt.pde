
//Endpoints of Line 1
float[] L1;

//Endpoints of Line 2
float[] L2;

//Random initial velocity vectors
float[] vels;

//Intersection point
float[] iPoint;

void setup() {
  
  size(640, 480);
  background(0);
  stroke(255);
  strokeWeight(4);
  smooth();
  
  L1 = new float[4];
  L2 = new float[4];
  
  iPoint = new float[2];
  
  vels = new float[8];
  
  for(int i = 0; i < 4; i++) {
   
    if ( ((i+1) % 2) == 0) {
      
      L1[i] = random(height);
      L2[i] = random(height);
      
    } else {
      
        L1[i] = random(width);
        L2[i] = random(width);
    }

  }

  for (int i = 0; i < 8; i++) 
    vels[i] = random(-2,2);
    
}

void draw() {
  
  background(0);
 
  moveEP(); 
  colDetect();
   
  stroke(255);  
  fill(255);
  
  line(L1[0], L1[1], L1[2], L1[3]);
  ellipse(L1[0], L1[1], 5, 5);
  ellipse(L1[2], L1[3], 5, 5);

  line(L2[0], L2[1], L2[2], L2[3]);
  ellipse(L2[0], L2[1], 5, 5);
  ellipse(L2[2], L2[3], 5, 5);
  
  if (intDetect()) {
    fill(255, 0, 0);
    stroke(255, 0, 0);
    ellipse(iPoint[0], iPoint[1], 10, 10);
  }
 
/* 

  line(x1, y1, x2, y2);
  ellipse(x1, y1, 5, 5);
  ellipse(x2, y2, 5, 5);

  line(u1, v1, u2, v2);  
  ellipse(u1, v1, 5, 5);
  ellipse(u2, v2, 5, 5);
  
*/
    
}

void moveEP() {
  
  for (int i = 0; i < 4; i++) {
    
    L1[i] += vels[i];
    L2[i] += vels[i+4];    
    
  }
  
}

void colDetect() {
  
  for (int i = 0; i < 4; i++) {
   
    if ( ((i+1) % 2) == 0) { //Dealing with Y coords
      
      if ((L1[i] < 0) || (L1[i] > height))
        vels[i] *= -1;
        
      if ((L2[i] < 0) || (L2[i] > height))
        vels[i+4] *= -1;
        
    } else {                //Dealing with X coords
      
      if ((L1[i] < 0) || (L1[i] > width))
        vels[i] *= -1;
        
      if ((L2[i] < 0) || (L2[i] > width))
        vels[i+4] *= -1;
        
    }
   
  }   
  
}

boolean intDetect() {
  
  float x1 = L1[0];
  float y1 = L1[1];  
  float x2 = L1[2];  
  float y2 = L1[3];

  float x3 = L2[0];
  float y3 = L2[1];  
  float x4 = L2[2];  
  float y4 = L2[3];  
  
  float denom  = (y4-y3) * (x2-x1) - (x4-x3) * (y2-y1);   
  float numera = (x4-x3) * (y1-y3) - (y4-y3) * (x1-x3);
  float numerb = (x2-x1) * (y1-y3) - (y2-y1) * (x1-x3);
  
  float t1 = numera / denom;
  float t2 = numerb / denom;
  
  if (t1 < 0 || t1 > 1 || t2 < 0 || t2 > 1)
    return false;
  else {

  iPoint[0] = x1 + t1 * (x2 - x1);
  iPoint[1] = y1 + t1 * (y2 - y1);  
  
  return true;
  
  }
  
}

  

  
  
  
