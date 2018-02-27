function main()
{
  $(".body").hide();
  $(".body").fadeIn(1000);
  $("#main").animate({top:"-=0"});
}

$(document).ready(main);

