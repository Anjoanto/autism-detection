<?php
    session_start();

    // echo $_SESSION["name"];
    // echo $_SESSION["out"];
    // $res =  json_decode($_SESSION["out"], true);
    // echo $res;
    $res = json_decode($_SESSION["out"]) ;

    $r = $res->result ;

    // echo $r;
?>

<!-- <img src="autisam.png" /> -->
<div>
<img src="http://localhost/site/pythonProject/aut.png" />
</div>

<div>
    <p style="color: blue; font-size: 46px;">
    <?php
    if( $res->result <= 0.5 ){
        echo "Hi ". $_SESSION["name"] . " Chance for autistic is high ( " . $r = $res->result . " )";
    }
    else{
        echo "NON AUTISTIC";
    }      
    ?>  
</p>
</div>