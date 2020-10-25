    <title>User Details</title> 
    <style> 
        table { 
            margin:  auto; 
            font-size: large; 
            border: 1px solid black; 
        } 
        h1 { 
            text-align: center; 
            color: #006600; 
            font-size: xx-large; 
            font-family: 'Gill Sans', 'Gill Sans MT',  
            ' Calibri', 'Trebuchet MS', 'sans-serif'; 
        } 
        td { 
            background-color: #E4F5D4; 
            border: 1px solid black; 
        } 
        th, 
        td { 
            font-weight: bold; 
            border: 1px solid black; 
            padding: 10px; 
            text-align: center; 
        } 
        td { 
            font-weight: lighter; 
        } 
    </style>  
<?php
session_start();

    define("DB_HOST", "localhost");
    define("DB_USER", "root");
    define("DB_PASSWORD", "");
    define("DB_DATABASE", "cyber_user");

 $db = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
 $sql="select * from details";
 $sql1=mysqli_query($db,$sql);
 ?>
<table>
<tr>
<th>Name</th>
<th>Age</th>
<th>Contact</th></tr>
<?php

while($details=mysqli_fetch_array($sql1)){?>
<tr>
<td align="center"><?php echo $details['name'];?></td>
<td align="center"><?php echo $details['age'];?></td>
<td align="center"><?php echo $details['contact'];?></td><tr>
<?php 
}?>
</table>