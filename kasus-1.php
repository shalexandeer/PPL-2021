<?php
 function pangkat(int $n) {
    $hasil = $n * $n;
    return $hasil; 
}
function Panjang($n){
   return strlen($n);
}
function Penjumlahan(int $n1, int $n2){
    return $n1 + $n2;
}
function Pengurangan(int $n1, int $n2){
    return $n1 - $n2;
}

echo pangkat(7).PHP_EOL;
echo Panjang('sistem');
echo Penjumlahan(10000,20000).PHP_EOL;
echo Pengurangan(120000, 20000)
?>
