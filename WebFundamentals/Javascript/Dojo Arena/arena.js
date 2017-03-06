$(document).ready(function(){

  $('#dojo').hover(function(){
    $('body').css("background-image","url('dojo.jpg')");
    $('#dojo').click(function(){
      $('body').css("background-image","url('dojo.jpg')");
      $('#arena_select').hide();
      $('#player_select').show()
    });
  });
  $('#beach').hover(function(){
    $('body').css('background-image','url("beach.jpg")');
    $('#beach').click(function(){
      $('body').css("background-image","url('beach.jpg')");
      $('#arena_select').hide();
      $('#player_select').show()
    });
  });
  $('#earth').hover(function(){
    $('body').css('background-image','url("earth.jpg")');
    $('#earth').click(function(){
      $('body').css("background-image","url('earth.jpg')");
      $('#arena_select').hide();
      $('#player_select').show()
    });
  });

  $('#matrix').hover(function(){
      $('body').css('background-image','url("matrix.jpg")');
      $('#matrix').click(function(){
        $('body').css("background-image","url('matrix.jpg')");
        $('#arena_select').hide();
        $('#player_select').show()
      });
    });

  $('#snow').hover(function(){
    $('body').css('background-image','url("snow.jpg")');
    $('#snow').click(function(){
      $('body').css("background-image","url('snow.jpg')");
      $('#arena_select').hide();
      $('#player_select').show()
    });
  });
  $('#forest').hover(function(){
      $('body').css('background-image','url("forest.jpg")');
      $('#forest').click(function(){
        $('body').css("background-image","url('forest.jpg')");
        $('#arena_select').hide();
        $('#player_select').show()
      });
    });
$(document).on('change','#first',function(){
  var player_1 = $('#first').val()+'.png'; //url.png
  $('.play #player_left').css("src", player_1);
  console.log(player_1);

    });
    $(document).on('change','#second',function(){
      var player_2 = $('#second').val()+'.png'; //url.png
      $('.play #player_right').css("src", player_2);
      console.log(player_2);

  });
});
