<?php

/**
 * File to handle all API requests
 * Accepts GET and POST
 * 
 * Each request will be identified by TAG
 * Response will be JSON data

  /**
 * check for POST request 
 */
 //echo 'erer';
  $host = "localhost";
  $user = "UserName";
  $pass = "Password";
  $db = "hosp_dev";
 
if (isset($_POST['tag']) && $_POST['tag'] != '') {
    // get tag
    $tag = $_POST['tag'];

	 $con = mysql_connect($host, $user, $pass);
        // selecting database
        mysql_select_db($db);
    // response Array
    $response = array("tag" => $tag, "success" => 0, "error" => 0);

    // check for tag type
    if ($tag == 'cobby') {
                
        
		$sql="SELECT * FROM test";
		
		
		
		$query=mysql_query($sql);
		$response['cobby']=array();
		while($row=mysql_fetch_array($query)){
		$temp=array();
		$temp['username']=$row['username'];
		$temp['password']=$row['password'];
		array_push($response['cobby'],$temp);
		
		}
				
            $response["success"] = 1;
            echo json_encode($response);
} 


}
?>
