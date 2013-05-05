  $(function() {
    //FOR TEMPLATING
    if (firstTime) {
      $('#subscription').hide();
      $('#hide').show();

    };
    var recommendation = $('#recommendations').children('ul');

    var items = data;
    $(items).each(function(i,item){
      var rating = Math.floor(item.rating);

      var stars="";
      for (var j = 0; j < rating; j++) {
        stars = stars+"<span>&#10022;</span>";
      };
      for (var j = 0; j < 10-rating; j++) {
        stars = stars + "<span>&#10023;</span>";
      };
      var array = item.genre.split('|');
      var tags = '<li><a href="#">'+array[0]+'</a></li>';

      var li = '<li class="span2"><div class="thumbnail" style="background-image:url(../static/img/banner.jpg)"><div class="caption">SuperNatural : A FICTION Series</div><div class="rating"></div></div></li>'
      recommendation.append('<li class="span2" data-id="'+item.seriesid+'"><div class="thumbnail" style="background-image:url('+item.poster+')"><div class="caption">'+item.name+'</div><ul class="tags">'+tags+'</ul></div><div class="rating">'+stars+'</div></li>');
    });

    //FOR CAPTIONS

    $('.thumbnail').on("click",function  () {
      console.log("clicked");
      var id = $(this).parent().data('id');
      console.log("tvshow"+id);
      window.location = "/tv_show/?show_id="+id;
    });
    $(".thumbnail").hover(//mouseenter
        function () {
          //$(this).transit({scale:1.1});
          var extra = $(this).find('.extra');

          if (extra.length) {
            extra.show();
            extra.transition({x:'200px'});
          };
          $(this).find('.caption').transit({rotateX:'0deg'},'slow');
        },
        function () {
          //$(this).transit({scale:1});
          $(this).find('.caption').transit({rotateX:'-90deg'},'fast');
        }
    );

//RATING
  });