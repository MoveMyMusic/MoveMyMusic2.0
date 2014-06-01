  $(function(){
 $("button#submit-sign-up").click(function(){
		 $.ajax({
            type: "POST",
        url: "signup.php",
        data: $('form#student-sign-up').serialize(),
            success: function(msg){			
					$(".modal-body").load("thanks.php #content");
					$("#submit-sign-up").hide();
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