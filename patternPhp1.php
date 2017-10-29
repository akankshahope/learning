<?php
//Patern Printing star at certain points to become a shape
$start = microtime(true);
$i=0;$j=0;
$t=8/2;

for($i=0;$i<=3;$i++){
  for($j=0;$j<=8;$j++) {
      
      if($j==0 || $j==$t || $j==8 || $i==$j || $j==8-$i){
       echo "*";
              //echo "    " ;      
            }
      else{
              echo "$";
            }
    }
  echo "<br>";
              
              
              
              
              
}
echo microtime(true) - $start;
?>
