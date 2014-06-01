  $(function(){
 $("button#submit-teacher-sign-up").click(function(){
		 $.ajax({
            type: "POST",
        url: "tsignup.php",
        data: $('form#teacher-sign-in').serialize(),
            success: function(msg){			
					$(".modal-body").load("thanks.php #content");
					$("#submit-teacher-sign-up").hide();
					$("div.container.sign-in-dialog").removeClass("sign-in-dialog");
					 			//reset values in all input fields
                    $('.signup input').val(''); 
                    $('.signup textarea').val(''); 
                    $('.signup select').val(''); 

                 },
        error: function(){
            alert("failure");
            }             
    });
});
})