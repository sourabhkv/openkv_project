<?php
    $name = $_post['name'];
    $visitor_email = $_POST['email'];
    
    $email_from = 'Irisfeedback@gmail.com';
    
    $email_subject = 'New Form Submission';

    $email_body = "User Name: $name.\n".
                    "User Message: $message.\n";
    
    $to = "rvarunabhics10@gmail.com"
    
    $headers = "From: $email_from \r\n";
    
    $headers .= "Reply-To: $visitor_email \r\n";

    mail($to,$email_subject,$email_body,$headers);

    header("Location: index.html");
?>