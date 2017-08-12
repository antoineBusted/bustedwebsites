jQuery(document).ready(function(){

    jQuery(".album-link").on("click",function(event){
        event.preventDefault();
        jQuery(this).closest(".album-list").find(".songlist").slideToggle();
    });

      jQuery(".song").on("click",function(event){
        event.preventDefault();
        var $songName = "."+jQuery(this).data("song");
        var $albumName = "."+jQuery(this).data("album");
        jQuery(".album-detail").find(".lyric-detail").hide();
        jQuery($albumName).find($songName).fadeToggle();
      });



});
