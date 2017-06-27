<?php
$start = microtime(true);
$i=0;
$j=0;
$t=4;
$last = 8;
for($i=0;$i<=3;$i++){
  for($j=0;$j<=8;$j++){
      if(in_array($j,array('0','4','8'))|| $j==$i || $j==$last-$i){
             echo '*';    
            }else{
             echo " ";
            }
    }
  echo "<br/>";
}
echo microtime(true) - $start;
?>