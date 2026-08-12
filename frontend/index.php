<html>

<head>
    <title>Autism</title>
    <link rel="stylesheet" href="button.css" />
</head>

<!-- <body style="background-color:rgb(13, 13, 14);"> -->
<body style="background-color: #8ebf42;"> 
    
    <div class="hor-ver-center">
     <form method="post">
      <label class="large"><b>Name :</b></Name></label> <input type="text" name="txtName" class="textbox" /> <br />
      <label class="seclarge"><b> Gender :</b> </label>
      <label class="container"> Male<input type="checkbox" checked="checked">
      <span class="checkmark"></span>
      </label><label class="container"> Female <input type="checkbox" checked="checked">
      <span class="checkmark"></span>
      </label> <br/> 
      <button type="submit" name="py" class="button" > <span> Get's  Started </span> </button>
     </form>
   </div>
      <div class="center" >
         <img src="anjo3.png" width="700px" height="350px">
      </div> 
      <?php
      session_start();
        if(isset($_POST["py"])){
          $_SESSION["name"] = $_POST["txtName"];
         
            // $command = escapeshellcmd('C:\Users\USER\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/USER/PycharmProjects/pythonProject/handTrack.py' );
            // $command = escapeshellcmd('C:\xampp\htdocs\site\pythonProject\venv\Scripts\python.exe C:\xampp\htdocs\site\pythonProject\handTrack.py');
            // $output = shell_exec($command);
            $curl = curl_init();
          curl_setopt($curl,CURLOPT_URL,'http://127.0.0.1:5000/track');
          curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
          $output = curl_exec($curl);
          curl_close($curl);

            $_SESSION["out"] = $output;
            header("Location: result.php");
            // echo "test";
            echo $output;
        }
    
     
    ?>    
     
</body>

</html>