$(document).ready(function(){
	$("#add_err").css('display', 'none', 'important');
	 $("button#submit-teacher-sign-in").click(function(){	
		  uname=$("#uname").val();
		  password=$("#tword").val();
		  $.ajax({
		   type: "POST",
		   url: "tlogin.php",
			data: "uname="+username+"&tpwd="+tpassword,
		   success: function(html){    
			if(html=='true')    {
			 //$("#add_err").html("right username or password");
			 window.location="dashboard.php";
			$("#submit-teacher-sign-in").hide();
			$("div.container.sign-in-dialog").removeClass("sign-in-dialog");

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