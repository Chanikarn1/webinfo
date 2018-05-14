var nav = document.getElementById("navbar");

window.scroll = function(){
if(window.pageYOffset > 100){
navbar.style.background= "#000000";
}
else{
navbar.style.background = "transparent";

}
}