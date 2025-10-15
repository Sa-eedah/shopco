$(document).ready(function(){
    $('.autoplay').slick({
        slidesToShow: 5,
        slidesToScroll: 5,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
      });

      $('.reviews').slick({
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        arrows: true,
        prevArrow:$(".arrowright"),
        nextArrow:$(".arrowleft"),

      });
});
