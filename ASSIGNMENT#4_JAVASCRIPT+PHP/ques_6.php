<?php
session_start();

    define("DB_HOST", "localhost");
    define("DB_USER", "root");
    define("DB_PASSWORD", "");
    define("DB_DATABASE", "cyber_user");

 $db = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);
 if($_POST){
   $chk="select * from data where phoneNo='".$_REQUEST['no']."'";
   $chk1=mysqli_query($db,$chk);
   if(mysqli_num_rows($chk1)){
  echo ("<script>alert('Phone No already exist');</script>");
   }
   else{
   $sql1="INSERT INTO details(name, age, contact) VALUES('".$_REQUEST['name']."','".$_REQUEST['age']."','".$_REQUEST['no']."')";
   mysqli_query($db,$sql1) or die('table not present');?>
   <script>
   alert('stored sucessfully');
   </script>
   <?php
   }
   }
?>
<form name="data" id="name" method="post" onsubmit="">
<table width="100%" border="0" cellspacing="0" cellpadding="5">
  <tr>
    <td width="20%" style="color: #333333"><b>NAME </B></label></td>
    <td width="70%"><input name="name" style=" font-size: 12px;border: 1px solid #333333;height: 22px;" type="text" id="name" value="" size="30" required/></td>
   </tr><tr>
       <td width="20%" style="color: #333333"><b>AGE</b></td>
       <td width="70%"><input name="age" style="font-size: 12px;border: 1px solid #333333;height: 22px;" type="number" id="age" value="" size="30" required /></td>
  </tr><tr>
  <td width="20%" style="color: #333333"><b>CONTACT</b></td>
  <td width="70%"><input name="no" style="font-size: 12px;border: 1px solid #333333;height: 22px;" type="tel" id="no" value="" size="30" required placeholder="0123456789" pattern="[0-9]{10}" /></td>
  </tr>
  <tr><td align:'center'>
  <button onclick="" type="submit" >CONFIRM </button></td></tr></table>
  </form>