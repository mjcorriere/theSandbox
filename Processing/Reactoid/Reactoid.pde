import ddf.minim.*;
import ddf.minim.signals.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;

Animation animation1;
float xpos, ypos;

boolean handleClick;

int fRate, initfRate, initFreq, curFreq;

Minim minim;
AudioOutput out;
SquareWave square;
LowPassSP lowpass;

void setup() {
  size(480, 800);
  background(0);
  
  handleClick = true;
  
  initfRate = 15;
  fRate = initfRate;
  
  initFreq = 110;
  curFreq = 110;
  
  frameRate(fRate);

  animation1 = new Animation("r_", 26);
  
  minim = new Minim(this);

  // get a stereo line out with a sample buffer of 512 samples
  out = minim.getLineOut(Minim.STEREO, 1024);

  // create a SquareWave with a frequency of 440 Hz,
  // an amplitude of 1 and the same sample rate as out
  square = new SquareWave(initFreq, 2, 44100);

  // create a LowPassSP filter with a cutoff frequency of 200 Hz
  // that expects audio with the same sample rate as out
  lowpass = new LowPassSP(200, 44100);

  // now we can attach the square wave and the filter to our output
  out.addSignal(square);
//  out.addEffect(lowpass);

}

void draw() { 

  animation1.display(0,0);

/*  if((mousePressed) && (animation1.getFrame() == 25)) {
    fRate += 5;
    frameRate(fRate);
    println("FrameRate: " + fRate);
  }
  */
  
}

void mousePressed() {

  if (handleClick) {

    if ((animation1.getFrame() == 25) || (animation1.getFrame() == 24) || (animation1.getFrame() == 0)) {
      fRate += 2;
      curFreq += 20;
      frameRate(fRate);
      println("FrameRate: " + fRate);
      square.setFreq(curFreq);
      
      handleClick = false;
    } else {
      
      fRate = initfRate;
      curFreq = initFreq;
    
      if(animation1.isPaused()) 
        animation1.unPause();
        else animation1.pause();

      frameRate(fRate);
      square.setFreq(initFreq);
      
      println("SWING AND A MISS");
      handleClick = false;
      
    }    
    
  }          
  
}

void mouseReleased() {
  
  handleClick = true;
  
}


class Animation {
  PImage[] images;
  int imageCount;
  int frame;
  String dir;
  boolean pause;
  
  Animation(String imagePrefix, int count) {

    pause = false;
    imageCount = count;
    images = new PImage[imageCount];
    
    dir = "C:\\Documents and Settings\\NotMark\\My Documents\\Reactoid Animate\\";

    for (int i = 0; i < imageCount; i++) {
      // Use nf() to number format 'i' into four digits
      String filename = dir + imagePrefix + nf(i+1, 2) + ".png";
      images[i] = loadImage(filename);
    }
  }

  void display(float xpos, float ypos) {
    
    if (pause == false)
      frame = (frame+1) % imageCount;

    image(images[frame], xpos, ypos);

  }
  
  int getWidth() {
    return images[0].width;
  }
  
  int getFrame() {
    return frame;
  }
  
  void pause() {
    pause = true;
  }
  
  void unPause() {
    pause = false;
  }
  
  boolean isPaused() {
    return pause;
  }
  
}
