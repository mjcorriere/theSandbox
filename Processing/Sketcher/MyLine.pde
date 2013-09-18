class MyLine {
  
  PVector v1, v2;

  MyLine(PVector _v1, PVector _v2) {
    
    v1 = new PVector();
    v2 = new PVector();
    
    v1.set(_v1);
    v2.set(_v2);   
   
  }

  void display() {
    

    fill(255);

    ellipse(v1.x, v1.y, 4, 4);
    ellipse(v2.x, v2.y, 4, 4);    

    stroke(255);
    strokeWeight(3);
    smooth();
    line(v1.x, v1.y, v2.x, v2.y);  
  
    noStroke();
    
  }  
  
}
