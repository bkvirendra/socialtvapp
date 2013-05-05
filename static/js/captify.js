//jQuery.fn.extend({captify:function(uo){var o=$.extend({speedOver:"fast",speedOut:"normal",hideDelay:500,animation:"slide",prefix:"",opacity:"0.45",className:"caption-bottom",position:"bottom",spanWidth:"100%"},uo);$(this).each(function(){var img=this;$(this).load(function(){if(img.hasInit){return false}img.hasInit=true;var over_caption=false;var over_img=false;var captionLabelSrc=$("#"+$(this).attr("rel"));var captionLabelHTML=!captionLabelSrc.length?$(this).attr("alt"):captionLabelSrc.html();captionLabelSrc.remove();var toWrap=this.parent&&this.parent.tagName=="a"?this.parent:$(this);var wrapper=toWrap.wrap("<div></div>").parent().css({overflow:"hidden",padding:0,fontSize:0.1}).addClass("caption-wrapper").width($(this).width()).height($(this).height());$.map(["top","right","bottom","left"],function(i){wrapper.css("margin-"+i,$(img).css("margin-"+i));$.map(["style","width","color"],function(j){var key="border-"+i+"-"+j;wrapper.css(key,$(img).css(key))})});$(img).css({border:"0 none"});var caption=$("div:last",wrapper.append("<div></div>")).addClass(o.className);var captionContent=$("div:last",wrapper.append("<div></div>")).addClass(o.className).append(o.prefix).append(captionLabelHTML);$("*",wrapper).css({margin:0}).show();var captionPositioning=jQuery.browser.msie?"static":"relative";caption.css({zIndex:1,position:captionPositioning,opacity:o.animation=="fade"?0:o.opacity,width:o.spanWidth});if(o.position=="bottom"){var vLabelOffset=parseInt(caption.css("border-top-width").replace("px",""))+parseInt(captionContent.css("padding-top").replace("px",""))-1;captionContent.css("paddingTop",vLabelOffset)}captionContent.css({position:captionPositioning,zIndex:2,background:"none",border:"0 none",opacity:o.animation=="fade"?0:1,width:o.spanWidth});caption.width(captionContent.outerWidth());caption.height(captionContent.height());var topBorderAdj=o.position=="bottom"&&jQuery.browser.msie?-4:0;var captionPosition=o.position=="top"?{hide:-$(img).height()-caption.outerHeight()-1,show:-$(img).height()}:{hide:0,show:-caption.outerHeight()+topBorderAdj};captionContent.css("marginTop",-caption.outerHeight());caption.css("marginTop",captionPosition[o.animation=="fade"||o.animation=="always-on"?"show":"hide"]);var cHide=function(){if(!over_caption&&!over_img){var props=o.animation=="fade"?{opacity:0}:{marginTop:captionPosition.hide};caption.animate(props,o.speedOut);if(o.animation=="fade"){captionContent.animate({opacity:0},o.speedOver)}}};if(o.animation!="always-on"){$(this).hover(function(){over_img=true;if(!over_caption){var props=o.animation=="fade"?{opacity:o.opacity}:{marginTop:captionPosition.show};caption.animate(props,o.speedOver);if(o.animation=="fade"){captionContent.animate({opacity:1},o.speedOver/2)}}},function(){over_img=false;window.setTimeout(cHide,o.hideDelay)});$("div",wrapper).hover(function(){over_caption=true},function(){over_caption=false;window.setTimeout(cHide,o.hideDelay)})}});if(this.complete||this.naturalWidth>0){$(img).trigger("load")}})}});

jQuery.fn.extend({
	captify: function (uo) {
		var o = $.extend({
			speedOver: "fast",
			speedOut: "normal",
			hideDelay: 500,
			animation: "slide",
			prefix: "",
			opacity: "0.45",
			className: "caption-bottom",
			position: "bottom",
			spanWidth: "100%"
		}, uo);
		$(this).each(function () {
			var img = this;
			$(this).load(function () {
				if (img.hasInit) {
					return false
				}
				img.hasInit = true;
				var over_caption = false;
				var over_img = false;
				var captionLabelSrc = $("#" + $(this).attr("rel"));
				var captionLabelHTML = !captionLabelSrc.length ? $(this).attr("alt") : captionLabelSrc.html();
				captionLabelSrc.remove();
				var toWrap = this.parent && this.parent.tagName == "a" ? this.parent : $(this);
				var wrapper = toWrap.wrap("<div></div>").parent().css({
					overflow: "hidden",
					padding: 0,
					fontSize: 0.1
				}).addClass("caption-wrapper").width($(this).width()).height($(this).height());
				$.map(["top", "right", "bottom", "left"], function (i) {
					wrapper.css("margin-" + i, $(img).css("margin-" + i));
					$.map(["style", "width", "color"], function (j) {
						var key = "border-" + i + "-" + j;
						wrapper.css(key, $(img).css(key))
					})
				});
				$(img).css({
					border: "0 none"
				});
				var caption = $("div:last", wrapper.append("<div></div>")).addClass(o.className);
				var captionContent = $("div:last", wrapper.append("<div></div>")).addClass(o.className).append(o.prefix).append(captionLabelHTML);
				$("*", wrapper).css({
					margin: 0
				}).show();
				var captionPositioning = jQuery.browser.msie ? "static" : "relative";
				caption.css({
					zIndex: 1,
					position: captionPositioning,
					opacity: o.animation == "fade" ? 0 : o.opacity,
					width: o.spanWidth
				});
				if (o.position == "bottom") {
					var vLabelOffset = parseInt(caption.css("border-top-width").replace("px", "")) + parseInt(captionContent.css("padding-top").replace("px", "")) - 1;
					captionContent.css("paddingTop", vLabelOffset)
				}
				captionContent.css({
					position: captionPositioning,
					zIndex: 2,
					background: "none",
					border: "0 none",
					opacity: o.animation == "fade" ? 0 : 1,
					width: o.spanWidth
				});
				caption.width(captionContent.outerWidth());
				caption.height(captionContent.height());
				var topBorderAdj = o.position == "bottom" && jQuery.browser.msie ? -4 : 0;
				var captionPosition = o.position == "top" ? {
					hide: -$(img).height() - caption.outerHeight() - 1,
					show: -$(img).height()
				} : {
					hide: 0,
					show: -caption.outerHeight() + topBorderAdj
				};
				captionContent.css("marginTop", -caption.outerHeight());
				caption.css("marginTop", captionPosition[o.animation == "fade" || o.animation == "always-on" ? "show" : "hide"]);
				var cHide = function () {
					if (!over_caption && !over_img) {
						var props = o.animation == "fade" ? {
							opacity: 0
						} : {
							marginTop: captionPosition.hide
						};
						caption.animate(props, o.speedOut);
						if (o.animation == "fade") {
							captionContent.animate({
								opacity: 0
							}, o.speedOver)
						}
					}
				};
				if (o.animation != "always-on") {
					$(this).hover(function () {
						over_img = true;
						if (!over_caption) {
							var props = o.animation == "fade" ? {
								opacity: o.opacity
							} : {
								marginTop: captionPosition.show
							};
							caption.animate(props, o.speedOver);
							if (o.animation == "fade") {
								captionContent.animate({
									opacity: 1
								}, o.speedOver / 2)
							}
						}
					}, function () {
						over_img = false;
						window.setTimeout(cHide, o.hideDelay)
					});
					$("div", wrapper).hover(function () {
						over_caption = true
					}, function () {
						over_caption = false;
						window.setTimeout(cHide, o.hideDelay)
					})
				}
			});
			if (this.complete || this.naturalWidth > 0) {
				$(img).trigger("load")
			}
		})
	}
});