/*
 * For toggle button to open and close nav menu for mobile
 */ 
$(function() {
  $(".toggle").on("click", function() {
      if ($(".item").hasClass("active")) {
          $(".item").removeClass("active");
          $(this).find("a").html("<i class='fas fa-bars'></i>");
      } else {
          $(".item").addClass("active");
          $(this).find("a").html("<i class='fas fa-times'></i>");
      }
  });
});