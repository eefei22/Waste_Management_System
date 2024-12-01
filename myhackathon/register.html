<?php

// Collect the form data sent via POST
$name = $_POST['username'];
$password = $_POST['password'];
$confirm_password = $_POST['confirm-password'];  $contact_info = $_POST['phone_number'];  
$role = $_POST['role'];  
// Debugging the POST data
echo "<pre>";
print_r($_POST);  // Display all form data
echo "</pre>";

// Check if all required fields are not empty
if ($password !== $confirm_password) {
    die('Error: Passwords do not match.');
}

if (!empty($name) && !empty($password) && !empty($contact_info) && !empty($role)) { // Check if all fields are non-empty
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "Wdhjbhgq@17@MySQL"; // Make sure this is the correct password for MySQL
    $dbname = "myhackathon";

    // Corrected database connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error); // More descriptive error message
    }

    // Table selection logic for role (Admin or Driver)
    if ($role == 'admin') {
        $SELECT = "SELECT admin_contact_info FROM admin WHERE admin_contact_info = ? LIMIT 1";
        $INSERT = "INSERT INTO admin (admin_name, admin_password, admin_contact_info) VALUES (?, ?, ?)";
    } else if ($role == 'garbage-truck-driver') {
        $SELECT = "SELECT driver_contact_info FROM driver WHERE driver_contact_info = ? LIMIT 1";
        $INSERT = "INSERT INTO driver (driver_name, driver_password, driver_contact_info) VALUES (?, ?, ?)";
    }

    // Prepare the statement to check for existing contact info
    $stmt = $conn->prepare($SELECT);
    $stmt->bind_param("s", $contact_info);
    $stmt->execute();
    $stmt->store_result();
    $rnum = $stmt->num_rows;

    if ($rnum == 0) {
        // If contact info is not found, insert into the appropriate table based on role
        $stmt->close();

        // Hash the password
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);

        // Prepare the insert statement based on role
        $stmt = $conn->prepare($INSERT);
        $stmt->bind_param("sss", $name, $hashed_password, $contact_info);

        // Debugging insert execution
        if ($stmt->execute()) {
            echo "New record inserted successfully as $role.";
        } else {
            echo "Error: " . $stmt->error;  // Display any insert error
        }
    } else {
        echo "Someone has already registered with this contact info.";
    }
    $stmt->close();
    $conn->close();
} else {
    echo "All fields are required.";  // This will notify if any fields are empty
    die();
}

?>

