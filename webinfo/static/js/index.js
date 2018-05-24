
  var slideIndex = 1;
  showSlides(slideIndex);
  
  // Next/previous controls
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  // Thumbnail image controls
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
  }
  
  var slideIndex = 0;
  carousel();

function carousel() {
    var i;
    var dots = document.getElementsByClassName("dot");
    var slides = document.getElementsByClassName("mySlides");
    
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
     dots[i].className = dots[i].className.replace(" active", "");
            }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(carousel,8000); // Change image every 2 seconds
} 

function myfunction(x){
    var a = document.getElementsByClassName("fa")[x];
    if (a.style.color == "red") {
        a.style.color = "gray";
    } else {
        a.style.color = "red";
    }
    // x.classList.toggle("fa fa-heart");
    }


    var slideIndex = 1;
    showDivs(slideIndex);
    
    function plusDivs(n) {
      showDivs(slideIndex += n);
    }
    
    function showDivs(n) {
      var i;
      var y = document.getElementsByClassName("mySlides2");
      var x = document.getElementsByClassName("mySlides");
      var z = document.getElementsByClassName("mySlides3");
      if (n > x.length) {slideIndex = 1}    
      if (n < 1) {slideIndex = x.length}
      for (i = 0; i < x.length; i++) {
         
         x[i].style.display = "none"; 
         y[i].style.display = "none"; 
         z[i].style.display = "none"; 
      }
      x[slideIndex-1].style.display = "inline";
      y[slideIndex-1].style.display = "inline"; 
      z[slideIndex-1].style.display = "inline"; 
    }



