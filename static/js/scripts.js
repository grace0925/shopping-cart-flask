$(function() {
    $('#1').prop('checked', true).change()
});

$(document).keypress(
  function(event){
    if (event.which == '13') {
      event.preventDefault();
    }
});