$(document).ready(function(){
	$("#add_err").css('display', 'none', 'important');
	 $("#sign-in").click(function(){	
		  fname=$("#fname").val();
		  lname=$("#lname").val();
		  password=$("#word").val();
		  $.ajax({
		   type: "POST",
		   url: "login.php",
			data: "fname="+fistname+"lname="+lastname+"&pwd="+password,
		   success: function(html){    
			if(html=='true')    {
			 //$("#add_err").html("right username or password");
			 window.location="dashboard.php";
			}
			else    {
			$("#add_err").css('display', 'inline', 'important');
			 $("#add_err").html("<img src='images/alert.png' />Wrong username or password");
			}
		   },
		   beforeSend:function()
		   {
			$("#add_err").css('display', 'inline', 'important');
			$("#add_err").html("<img src='images/ajax-loader.gif' /> Loading...")
		   }
		  });
		return false;
	});
});