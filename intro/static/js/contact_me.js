// Contact Form Scripts


// CSRF
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});*/

$(function() {

    var form = $('#contactForm');

    $("#contactForm input,#contactForm textarea").jqBootstrapValidation({

        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            // get values from FORM
            var name = $("input#name").val();
            var email = $("input#email").val();
            var phone = $("input#phone").val();
            var message = $("textarea#message").val();
            var captcha = $("textarea#g-recaptcha-response").attr("value");
            var captchaResponse = grecaptcha.getResponse();
            console.log(captchaResponse);
            //var firstName = name; // For Success/Failure Message*/
            // Check for white space in name for Success/Fail message
            /*if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }*/

            $.ajax({
//                url: "././mail/contact_me.php",
                url: '',
                type: form.attr('method'),
                data: {
                    
                    name: name,
                    phone: phone,
                    email: email,
                    message: message,
                    captcha: captcha,
                },
                //form.serialize(),
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        console.log("Hello from Firefox code");
                    }
                },
                cache: false,
                success: function() {
                    // Success message
                    /*$('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-success')
                        .append("<strong>Your message has been sent. </strong>");
                    $('#success > .alert-success')
                        .append('</div>');*/

                    new PNotify({
                        //title: 'Your message has been sent.',
                        text: 'Your message has been sent !',
                        type: 'success',
                        icon: 'fa fa-check',
                        styling: 'fontawesome'
                    });

                    //clear all fields
                    $('#contactForm').trigger("reset");
                    grecaptcha.reset();
                },
                error: function() {
                    // Fail message
                    /*$('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-danger').append("<strong>Sorry " + name + ", it seems that my mail server is not responding. Please try again later!");
                    $('#success > .alert-danger').append('</div>');*/
                    //clear all fields

                    new PNotify({
                        //title: 'Oops!',
                        text: 'Sorry ' + name + ', it seems that our mail server is not responding. Please try again later!.',
                        type: 'alert',
                        icon: 'fa fa-ban',
                        styling: 'fontawesome'
                    });

                    $('#contactForm').trigger("reset");
                    grecaptcha.reset();
                },
            });
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    /*$("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });*/
});

/*When clicking on Full hide fail/success boxes */
/*$('#name').focus(function() {
    $('#success').html('');
});*/
