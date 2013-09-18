class Ship {
  
  boolean movingUp, movingDown, movingLeft, movingRight;
  
  PImage imgShip, imgShipUp, imgShipUpHalf, imgShipDown,
            imgShipDownHalf;
            
  int x, y;
  
  int imgWidth, imgHeight;
  
  static final int velocity = 2;
  
  int motionStartTime;
            
  Ship(int _x, int _y) {
    
    this.x = _x;
    this.y = _y;
    
    motionStartTime = 0;
    
    movingUp = movingDown = movingLeft = movingRight = false;

    imgShip = loadImage("imgs/ship.png");    
    imgShipUp = loadImage("imgs/shipUp.png");
    imgShipUpHalf = loadImage("imgs/shipUpHalf.png");
    imgShipDown = loadImage("imgs/shipDown.png");
    imgShipDownHalf = loadImage("imgs/shipDownHalf.png"); 
  
    imgWidth = imgShip.width;
    imgHeight = imgShip.height;  
    
  }
  
  void update() {
    
    if (movingUp) {
      y -= velocity;
    } else if (movingDown) {
      y += velocity;
    }
    
    if (movingLeft) {
      x -= velocity;
    } else if (movingRight) {
        x += velocity;
    }   
    
  }
  
  void display() {
    
    int deltaT = millis() - motionStartTime;

    if (deltaT > 300 && deltaT <= 600) {
      if (movingUp)
        image(imgShipUpHalf, x - imgWidth/2, y - imgHeight/2);
      else if (movingDown)
        image(imgShipDownHalf, x - imgWidth/2, y - imgHeight/2);
      else {
        image(imgShip, x - imgWidth/2, y - imgHeight/2);    
      }            
    }

    else if (deltaT > 500) {
      if (movingUp)
        image(imgShipUp, x - imgWidth/2, y - imgHeight/2);
      else if (movingDown)
        image(imgShipDown, x - imgWidth/2, y - imgHeight/2); 
      else {
        image(imgShip, x - imgWidth/2, y - imgHeight/2);    
      }    
    }
    
    else {
      image(imgShip, x - imgWidth/2, y - imgHeight/2);    
    }  
        
      
      
  }
 
  void setUpState(int _state) {
    
    //_state 0 = stop moving up
    //_state 1 = move up
    
    if(_state == 1) {

      if (movingUp == false) {
            motionStartTime = millis();
      }            

      movingUp = true;

    }

    else movingUp = false;

  }
  
  void setDownState(int _state) {
    
    //_state 0 = stop moving down
    //_state 1 = move down
    
    if(_state == 1) {
      if (movingDown == false)      
        motionStartTime = millis();
      movingDown = true;
        
    }      
      else movingDown = false;
    
  }
  
  void setLeftState(int _state) {
    
    //_state 0 = stop moving up
    //_state 1 = move up    
    
    if(_state == 1)
      movingLeft = true;
      else movingLeft = false;    
    
    
  }
  
  void setRightState(int _state) {
    
    //_state 0 = stop moving up
    //_state 1 = move up 
    
    if(_state == 1)
      movingRight = true;
      else movingRight = false;    
    
  }
  
}
