Class MyVertex {
 
  PVector xy;
  color fillColor;
  
  MyVertex(int x, int y) {
   
    xy = new PVector(x, y);
    fillColor = color((float) x/width * 255, (float) y/height * 255, 0);    
    
  }
  
  void display() {

    fill(fillColor);
    ellipse(xy.x, xy.y, 6, 6);    
    
  }  
  
}
