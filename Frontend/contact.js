 $(function() {
//twitter bootstrap script
    $("button#contact-us-form-submit").click(function(){
            $.ajax({
            type: "POST",
        url: "process.php",
        data: $('form.contactForm').serialize(),
            success: function(msg){
                     $("#thanks").html(msg)
                    $("#form-content").modal('hide');    
                 },
        error: function(){
            alert("failure");
            }
              });
    });
});