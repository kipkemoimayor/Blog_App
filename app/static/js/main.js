$(document).ready(function () {
  $("#update").click(function(){
    Swal.fire({
    type: 'success',
    title: 'Success',
    text: 'Profile Updated ',
    timer:2000,
    showConfirmButton:false
  })
  })
  // $("#submit").click(function () {
  //   Swal.fire({
  //   type: 'success',
  //   title: 'Success',
  //   timer:2000,
  //   showConfirmButton:false
  // })
  //
  // })

  $(".title").mouseover(function(){
    $("span").show()

  })
  $("#delete").click(function(){
    alert("are you sure")
    // Swal.fire({
    // type: 'warning',
    // title: 'Login Required',
    // text: 'Please Login to Post your Idea',
    // html:'<a class="btn default-color" href="/authenticate/login">Sign in</a>',
    // showConfirmButton:false
  })
  $(".profile").hide()
  $("#change").show()
  })

  /*business logig*/

  $("#aii").click(function(){
    $("#AI").show()
    $("#D").hide()
    $("#R").hide()
    $("#IoT").hide()
    $("html,body").animate({scrollTo:$(document).height()},2000);
    return false;

  })




})
