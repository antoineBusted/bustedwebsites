

<?php


$albums = simplexml_load_file("../songs.xml");



?><div class="albums"><?php
foreach ($albums as $album){
  $albumName = $album["name"];
  $albumNameDash = str_replace(" ","-",$albumName);
  ?><div class="album-list"><a a href="#" class="album-link <?php echo $albumName?>" ><img src="../../lyrics/<?php echo strtolower($albumNameDash) ?>.jpg" class="coverart-list"/><h3><?php echo $albumName ?> ( <?php echo $album["year"] ?> )</h3>
    <div class="songlist"><ul><?php
  foreach ($album->song as $song) {
    $songNameDash = str_replace(" ","-",$song["name"]);
    ?><li><a href="#" class="song" data-song="<?php echo $songNameDash?>" data-album="<?php echo $albumNameDash?>"><?php echo $song["name"]?></a></li><?php
  }?></ul></div><?php
?></div><?php
}

?></div>

<div class="lyrics">
<? //Start albums
foreach ($albums as $album){
  $albumName = $album["name"];
  $albumNameDash = str_replace(" ","-",$albumName);
  ?><div class="album-detail <?php echo $albumNameDash?> ">
        <?php //start songs
            foreach ($album->song as $song) {
              $songName = $song["name"];
              $songNameDash = str_replace(" ","-",$song["name"]);
            ?><div class="lyric-detail <?php echo $songNameDash?>">
              <img src="../../lyrics/<?php echo strtolower($albumNameDash) ?>.jpg" class="coverart-detail"/>
              <h1><?php echo $albumName ?> - <?php echo $songName?></h1>
              <p class="infos"><?php echo $album["year"] ; if (isset($song["credits"])) {?> - credits : <?php echo $song["credits"]; }
                 if (isset($album["buy"])) {?> - <a href="<?php echo $album["buy"]?>" target="_blank">Buy this album</a><?php }

            ?></p>
                <?php //start lyrics
                 foreach ($song->part as $part) {
                  ?><div class="part <?php echo $part['type']?>"><pre><?php echo $part?></pre></div>

                  <?php
                }//End lyrics?>


            </div><?php
          }//End songs?>

  </div><?php }//End albums ?>



</div>
