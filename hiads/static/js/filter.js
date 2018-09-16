$(document).ready(function() {

  $('span:contains("all")').addClass('active');

  $('span:contains("all")').click(function() {
  $('span:not(:contains("all"))').removeClass('active');
    $(this).addClass('active');
    $('.tab').show(500)
  });

  $('span:contains("web design")').click(function() {
    $('span:not(:contains("web design"))').removeClass('active');
    $(this).addClass('active');
    $('.tab:contains("Web Design")').show(500);
    $('.tab:not(:contains("Web Design"))').hide(500);

  });

  $('span:contains("app design")').click(function() {
    $('span:not(:contains("app Design"))').removeClass('active');
    $(this).addClass('active');
    $('.tab:contains("App Design")').show(500);
    $('.tab:not(:contains("App Design"))').hide(500);
  });

  $('span:contains("icons")').click(function() {
    $('span:not(:contains("icons"))').removeClass('active');
    $(this).addClass('active');
    $('.tab:contains("Icons")').show(500);
    $('.tab:not(:contains("Icons"))').hide(500);
  });

  $('span:contains("logo")').click(function() {
    $('span:not(:contains("logo"))').removeClass('active');
    $(this).addClass('active');
    $('.tab:contains("Logo")').show(500);
    $('.tab:not(:contains("Logo"))').hide(500);
  });

  $('span:contains("brochure design")').click(function() {
    $('span:not(:contains("brochure design"))').removeClass('active');
    $(this).addClass('active');
    $('.tab:contains("Brochure Design")').show(500);
    $('.tab:not(:contains("Brochure Design"))').hide(500);
  });

});
