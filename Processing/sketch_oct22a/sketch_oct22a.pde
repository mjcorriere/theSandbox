import processing.opengl.*;

PFont fontCalibri;

String drawMode;
color fillColor;
boolean mouseDown;

ArrayList verticies;

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
    
  drawMode = "Vertex";
  
  frameRate(100);
   
}

void draw() {
  
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
        
//        verticies.add(new MyVertex(mouseX, mouseY));
        
//        fill(fillColor);
//        ellipse(mouseX, mouseY, 6, 6);
      }
      
    }
    
    else if(drawMode == "Line") {
      
      
    
    }
    
    mouseDown = false;
    
  }
  
//  drawVerticies();
////  drawLines();
  
}

//void drawVerticies() {
//  
////  for(i = 0; i < verticies.size(); i++)
////    (MyVertex) verticies.get(i).display();
//
//}

void mousePressed() {
 
  mouseDown = true;
  
  //fill(fillColor);
  //ellipse(mouseX, mouseY, 25, 25);
  
  //fill(225);
  //text("(" + str(mouseX) + ", " + str(mouseY) + ")", mouseX, mouseY);
  
}

void mouseReleased() {
  
  mouseDown = false;
  
}

void keyPressed() {
  
  if (key == 'V' || key == 'v')
    drawMode = "Vertex";
    
  if (key == 'L' || key == 'l')
    drawMode = "Line";
    
}
