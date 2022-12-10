<?php 
    function samaDengan($n1,$n2){
        $hasil = $n1 == $n2;
        return $hasil;
    }
    
    function lebihBesar($n1,$n2){
        $hasil = $n1 > $n2;
        return $hasil;
    }
    
    function lebihKecil($n1,$n2){
        $hasil = $n1 < $n2;
        return $hasil;
    }
    
    function tidakSama($n1,$n2){
        $hasil = $n1 != $n2;
        return $hasil;
    }
    
    function perbandingan($n1,$n2){
        echo 'Nilai A adalah '.$n1.PHP_EOL;
        echo 'Nilai B adalah '.$n2.PHP_EOL;
        echo 'A pangkat B adalah '.$n1**$n2.PHP_EOL;
        echo 'A modulus B adalah '.$n1%$n2.PHP_EOL;
        echo "A sama dengan B adalah ". (samaDengan($n1,$n2) ? "true" : "false").PHP_EOL;
        echo "A lebih besar dari B adalah ". (lebihBesar($n1,$n2) ? "true" : "false").PHP_EOL;
        echo "A lebih besar dari B adalah ". (lebihKecil($n1,$n2) ? "true" : "false").PHP_EOL;
        echo "A tidak sama dengan B adalah ". (tidakSama($n1,$n2) ? "true" : "false").PHP_EOL;
    }
    
    perbandingan(9,2);
?>