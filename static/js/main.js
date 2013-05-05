/* 

	Authored by: Virendra Rajput
	Twitter: @bkvirendra
	Email: virendra.rajput567@gmail.com

*/

/* the autocomplete search */
  $(function() {

    $("#search").autocomplete({
      source: "/search",
      minLength: 1,
      focus: function( event, ui ) {
        $("#search").val( ui.item.title );
        return false;
      },
      select: function( event, ui ) {
        //var title = ui.item.title;
        $("#search").val(ui.item.title);
        window.location = "/show/" + ui.item.title.replace(' ','-');
        return false;
      }
    })
    .data('ui-autocomplete')._renderItem = function(ul, item) {
      try {
        cast =  "Starring: " + eval(item.regular_cast).slice(0,2).join(', ') + "<br>";
      } catch(e) {
        cast = "";
      }
      try {
        if (item.program_creator && item.program_creator != "-") {
          creator = "Creator: " + item.program_creator;
        } else {
          creator = "";
        }
      } catch(e) {
        creator = "";
      }
      return $("<li class='ui-menu-item' role='menuitem'>").data('item.autocomplete', item)
        .append("<a class='ui-corner-all' tabindex='-1' href='#'><img src='" + item.image_thumbnail + "'><span><h4>" + item.title + "\
          </h4><small>" + cast + creator + "</small></span></a>")
        .appendTo(ul);
    };

  });

