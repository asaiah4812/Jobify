// change navbar color

$(document).ready(function() {
    $(window).scroll(function(){
        var scroll = $(window).scrollTop();
        if(scroll>150) {
            $(".navbar").css("background", "#222");
            $(".navbar").css("box-shadow", "rgba(0,0,0,0.3) 0px 4px 12px")
        }
        else {
            $('.navbar').css('background', 'transparent');
            $('.navbar').css('box-shadow','none');
        }
    })
} )


const mobile = document.querySelector(".menu-toggle");
const mobileLink = document.querySelector(".navbar-menu");

mobile.addEventListener("click", function(){
    mobile.classList.toggle("is-active");
    mobileLink.classList.toggle("active");
})

mobileLink.addEventListener("click", function(){
    const menuBars = document.querySelector(".is-active");
    if(window.innerWidth <=768 && menuBars) {
        mobile.classList.toggle("is-active");
        mobileLink.classList.remove("active");
    }
})

// console.log("hello")

// function changeNavbarStyle() {
//   // when window scrolls
//   $(window).scroll(function () {
//     // get scroll position
//     var scroll = $(window).scrollTop();
//     // if scroll position is greater than 150
//     if (scroll > 150) {
//       // set navbar background color and box-shadow
//       $(".navbar").css("background", "#222");
//       $(".navbar").css("box-shadow", "rgba(0,0,0,0.1) 0px 4px 12px");
//     }
//     // if scroll position is less than or equal to 150
//     else {
//       // set navbar background color and box-shadow to transparent
//       $(".navbar").css("background", "transparent");
//       $(".navbar").css("box-shadow", "none");
//     }
//   });
// }