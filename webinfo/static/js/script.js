$(document).ready(function(){
    $(".animatedButton").on('click',function(){
        $(this).addClass("animate");
        setTimeout(function(){
            $(".animatedButton").removeClass("animate");
        },500);
    });
});
