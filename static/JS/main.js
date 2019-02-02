/*global $*/


$("#animate").click(function(){
    var x = $("#animate").offset();
    var y = x.left / 2;
    var width = document.getElementById('heroesdiv').offsetWidth / 2;
    var final_number = width - y;
    
    $("#animate").animate({
        left: final_number
    }, 3000);
});

