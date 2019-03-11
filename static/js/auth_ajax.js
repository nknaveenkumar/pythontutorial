/*Employee Registration code*/

 $(document).ready(function(){

    $('#signup').on('click', function(e){
        e.preventDefault();

        var uniqueid = new Date().getUTCMilliseconds();

        $name = $('#username').val();
        $email = $('#emails').val();
        $password = $('#password').val();
        $phone = $('#phone').val()

        if(IsEmail($email)==false){
          $('#success').text("invalid email id");
          return false;
         }

        if( $('#username').val() == "" || $('#emails').val() == "" || $('#password').val() == "" || $('#phone').val()=="" )
             {
            $('#success').text("Please fill the fields*");
             return false;
        }

        else{
            $.ajax({
                type: "POST",
                url : "/registration",
                enctype: "multipart/form-data",
                cache : false,
                data: {

                    uniqueid,
                    name: $name,
                    email: $email,
                    password: $password,
                    phone:$phone,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

                },

                success: function(data){
                 $('#success').text(data);


                }
            });

          }

       });

    });

  /*Email validation*/

 function IsEmail(email) {
  var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if(!regex.test(email)) {
    return false;
  }else{
    return true;
  }
}



/* Login form */

   $(document).ready(function(){

      $('#login').on('click',function(e){
          e.preventDefault();

       console.log("start");

       $email=$('#emails').val();
       $password=$('#password').val();

        if($('#emails').val()=="" || $('#password').val()==""){
           alert("please fill the all fields..")
        }

        else {

        $.ajax({
          type: "POST",
          url: "/member_login",
          data: {
               email:$email,
               password:$password,
               csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
          },

           success:function(data){
           if (data){
            window.location=data
           }
          else{
          error="You Enter Wrong email and password"
           $('#error').text(error);
          }

       }
        });
      }
   });
 });

