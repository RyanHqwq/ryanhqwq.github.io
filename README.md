<!DOCTYPE html>
<!-- saved from url=(0035)https://www.ddosi.com/V/index2.html -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>超绚丽多色彩发光立方体旋转动画</title>

<style>
body {
  margin: 0;
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  background: #222;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
      flex-wrap: wrap;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.world {
  -webkit-perspective: 800px;
          perspective: 800px;
  width: 100vh;
  height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
      flex-wrap: wrap;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.cube {
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
  width: 50vh;
  height: 50vh;
  position: relative;
  -webkit-animation: rotator 1s linear infinite;
          animation: rotator 1s linear infinite;
  outline: 0;
}
.cube * {
  background: #000;
  box-shadow: 0 0 3vh currentColor;
  -webkit-transition: background 0.4s ease-in-out, box-shadow 0.4s ease-in-out;
  transition: background 0.4s ease-in-out, box-shadow 0.4s ease-in-out;
}
.cube:hover * {
  background: currentColor;
  box-shadow: 0 0 20vh currentColor;
}
.cube .cube__front {
  color: deeppink;
  -webkit-transform: translateZ(25vh);
          transform: translateZ(25vh);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.cube .cube__right {
  color: lightcoral;
  -webkit-transform: rotateY(90deg) translateZ(25vh);
          transform: rotateY(90deg) translateZ(25vh);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.cube .cube__left {
  color: skyblue;
  -webkit-transform: rotateY(270deg) translateZ(25vh);
          transform: rotateY(270deg) translateZ(25vh);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.cube .cube__back {
  color: seagreen;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  -webkit-transform: rotateY(180deg) translateZ(25vh);
          transform: rotateY(180deg) translateZ(25vh);
}
.cube .cube__top {
  color: mediumseagreen;
  -webkit-transform: rotateX(90deg) translateZ(25vh);
          transform: rotateX(90deg) translateZ(25vh);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.cube .cube__bottom {
  color: dodgerblue;
  -webkit-transform: rotateX(270deg) translateZ(25vh);
          transform: rotateX(270deg) translateZ(25vh);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

@-webkit-keyframes rotator {
  0% {
    -webkit-transform: rotateX(0deg) rotateY(0deg);
            transform: rotateX(0deg) rotateY(0deg);
  }
  100% {
    -webkit-transform: rotateX(360deg) rotateY(360deg);
            transform: rotateX(360deg) rotateY(360deg);
  }
}

@keyframes rotator {
  0% {
    -webkit-transform: rotateX(0deg) rotateY(0deg);
            transform: rotateX(0deg) rotateY(0deg);
  }
  100% {
    -webkit-transform: rotateX(360deg) rotateY(360deg);
            transform: rotateX(360deg) rotateY(360deg);
  }
}
</style>
</head>
<body oncontextmenu="self.event.returnValue=false" onselectstart="return false">

<div class="world">
  <div class="cube" tabindex="0">
    <div class="cube__front"></div>
    <div class="cube__back"></div>
    <div class="cube__left"></div>
    <div class="cube__right"></div>
    <div class="cube__top"></div>
    <div class="cube__bottom"></div>
  </div>
</div>






</body></html>
