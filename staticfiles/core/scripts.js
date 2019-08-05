$(document).ready(function(){

  $('.section-one').hover(function() {
    $('.container-fluid').toggleClass('one-is-active');
    document.getElementById("q2").css("font_size", "30px");
    document.getElementById("q1").style.display = "block";
  });

  $('.section-two').hover(function() {
    $('.container-fluid').toggleClass('two-is-active');
    document.getElementById("q1").css("font_size", "30px");
    document.getElementById("q2").style.display = "block";
  
  });
  $('.scroll').click(function() {
    $('html, body').animate({
          scrollTop: $(".container-fluid").offset().top
      }, 800);
  });




});