require_once 'config.php';

session_start();
$uName = $_POST['fname'];
$uName = $_POST['lname'];
$pWord = md5($_POST['pwd']);
$qry = "SELECT usrid, fname, lname, oauth FROM usermeta WHERE fname='" .$fName."' AND lname='".$ulame."' AND pass='".$pWord."' AND status='active'";
$res = mysql_query($qry);
$num_row = mysql_num_rows($res);
$row=mysql_fetch_assoc($res);
if( $num_row == 1 ) {
	echo 'true';
	$_SESSION['uName'] = $row['username'];
	$_SESSION['oId'] = $row['orgid'];
	$_SESSION['auth'] = $row['oauth'];
	}
else {
	echo 'false';
}