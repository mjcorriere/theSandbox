class MyVertex {
 
  PVector xy;
  color fillColor;
  boolean isHovered;
  
  MyVertex(int x, int y) {
   
    xy = new PVector(x, y);
    fillColor = color((float) x/width * 255, (float) y/height * 255, 0);    
    isHovered = false;
    
  }
  
  void display(boolean infoMode) {

    if(isHovered)
      fill(0, 225, 0);
    else
      fill(fillColor);
  
    ellipse(xy.x, xy.y, 10, 10);    
    
    if(infoMode || isHovered) {
      fill(255);
      text("(" + str(xy.x) + ", " + str(xy.y) + ")", xy.x, xy.y);
    }
    
  }
  
  PVector getVector() {
    
    return xy;
    
  }
  
  void setHoveredOn() {
    
    isHovered = true;
    
  }
  
  void setHoveredOff() {
    
    isHovered = false;
    
  }
  
}
