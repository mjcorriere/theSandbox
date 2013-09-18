import processing.opengl.*;

PFont fontCalibri;

String drawMode;
color fillColor;
boolean mouseDown;

ArrayList verticies;
ArrayList lynes;

boolean isFirstPoint;
boolean infoMode;
boolean isSnapped;

PVector initialLinePoint;
PVector snapVector;

void setup() {

  size(640, 480, OPENGL);
  background(35, 35, 55);
  
  noStroke();
  smooth();
  
  fontCalibri = loadFont("Calibri-Bold-18.vlw");
  textFont(fontCalibri);
  
  fillColor = color(0, 0, 0);
  mouseDown = false;
  
  verticies = new ArrayList();
  lynes = new ArrayList();
  
  initialLinePoint = new PVector();
  isFirstPoint = true;
  
  snapVector = new PVector();
  isSnapped = false;
    
  drawMode = "Vertex";
  
  frameRate(100);
   
}

void draw() {
  
  background(35, 35, 55);

  fill(80, 80, 100);
  rect(0, 0, width, 45);
  
  fill(225);
  
  textAlign(LEFT);
  
  String sx = "MouseX: " + str(mouseX);
  String sy = " MouseY: " + str(mouseY);

  text(sx + sy, 5, 5, 100, 35);
  
  text("DrawMode: " + drawMode, 125, 5, 200, 15);
  textAlign(RIGHT);
  
  text("Color:", 214, 35);
  
  fillColor = color((float)mouseX/width * 255, (float) mouseY/height*255, 0);
  
  fill(fillColor);
  rect(218, 25, 40, 12);
  
  if(mouseDown) {
    
    if(drawMode == "Vertex") {

      if(mouseY >= 45) {
        
        verticies.add(new MyVertex(mouseX, mouseY));
        
      }
      
    }
    
    else if(drawMode == "Line") {
      
      int lineX, lineY;
      
      if (isSnapped) {
        lineX = (int) snapVector.x;
        lineY = (int) snapVector.y;
      } else {
          lineX = mouseX;
          lineY = mouseY;
      }        

      if(isFirstPoint) {
        initialLinePoint.set((float)lineX, (float)lineY, 0);    
        isFirstPoint = false;
      }
      
      else {
        lynes.add(new MyLine(initialLinePoint, new PVector(lineX, lineY)));
        isFirstPoint = true;
      }
      
    }
    
    mouseDown = false;
    
  }
  
  detectVertexHover();

  drawLines();
  drawVerticies();

  
}

void detectVertexHover() {
  
  boolean foundSnap = false;
  
  int collisionRadius = 10;
  
  for(int i = 0; i < verticies.size(); i++) {
    MyVertex tempVertex = (MyVertex) verticies.get(i);

    PVector locationVector = new PVector();
    locationVector.set(tempVertex.getVector());
    
    float dist2 = pow((mouseX - locationVector.x), 2) + pow((mouseY - locationVector.y), 2);
    float collisionRadius2 = pow(collisionRadius, 2);
    
    if( dist2 < collisionRadius2 ) {
      tempVertex.setHoveredOn();
      setSnap(locationVector);

      foundSnap = true;

    }
    
  //FIGURE OUT WHY THIS PORTION IS BROKEN
  
  //Trace through the logic step by step.
  //You have a lot of pieces spread around and there is probably an unforseen
  //interaction. The code is messy (on purpose) and therefore the program flow
  //is getting out of hand. Slow down and check it out.

    else {
      tempVertex.setHoveredOff();
      print("foundSnap: " + str(foundSnap) + "\n");
      if(foundSnap = false)
        clearSnap();
    }
    
  }
 
}

void setSnap(PVector _snapVector) {
  
  snapVector.set(_snapVector);
  isSnapped = true; 
  print("snapping to " + str(snapVector.x) + ", " + str(snapVector.y) + "\n");
  
}

void clearSnap() {
  
  isSnapped = false;
  
  print("snap cleared\n");
  
}

void drawVerticies() {
  
  for(int i = 0; i < verticies.size(); i++) {
    MyVertex tempVertex = (MyVertex) verticies.get(i);
    tempVertex.display(infoMode);
  }

}

void drawLines() {
  
  if(!isFirstPoint) {
    strokeWeight(3);
    stroke(255);    
    line(initialLinePoint.x, initialLinePoint.y, mouseX, mouseY);
    noStroke();
  }

  for(int i = 0; i < lynes.size(); i++) {
    MyLine tempLine = (MyLine) lynes.get(i);
    tempLine.display();
  }  
  
}

void clearAll() {
  
  for (int i = verticies.size()-1; i >= 0; i--) {
    verticies.remove(i);
  }
  
  for (int i = lynes.size()-1; i >= 0; i--) {
    lynes.remove(i);
  }
  
}

void toggleInfoMode() {
  
  infoMode = !infoMode;
  
}


void mousePressed() {
 
  mouseDown = true;

}

void mouseReleased() {
  
  mouseDown = false;
  
}

void keyPressed() {
  
  if (key == 'V' || key == 'v')
    drawMode = "Vertex";
    
  if (key == 'L' || key == 'l')
    drawMode = "Line";
    
  if (key == 'C' || key == 'c')
    clearAll();
    
  if (key == 'I' || key == 'i')
    toggleInfoMode();
    
}
