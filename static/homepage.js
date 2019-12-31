function Admin_Login(){
    location.href = "/login/"
}
function Admin_Signup() {
    location.href = "/Signup/"
}
function Registered_As() {
    var registered_as = $("#registered_as option:selected").text();
    if (registered_as == "Student") {
        $("#student_admission_year").show();
        $("#student_course").show();
        $("#student_semesters").show();
        $("#student_sections").show();
    } else {
        $("#student_admission_year").hide();
        $("#student_course").hide();
        $("#student_semesters").hide();
        $("#student_sections").hide();
    }
}


$("#registered_as").change(function () {
    $("#err_registered_as").hide();
});
$("#first_name").keyup(function () {
    $("#err_first_name").hide();
});
$("#middle_name").keyup(function () {
    $("#err_middle_name").hide();
});
$("#last_name").keyup(function () {
    $("#err_last_name").hide();
});
$("#email").keyup(function () {
    $("#err_email").hide();
    $("#err_email_already").hide();
    $("#err_email_valid").hide();
});
$("#phone_no").keyup(function () {
    $("#err_phone_no").hide();
    $("#err_phone_no_valid").hide();
    $("#err_phone_no_already").hide();
});
$("#course").change(function () {
    $("#err_course").hide();
});
// $("#specialization").change(function(){
//  $("#err_specialization").hide();
// });
$("#semesters").change(function () {
    $("#err_semesters").hide();
});
$("#sections").change(function () {
    $("#err_sections").hide();
});
$("#admission_year").keyup(function () {
    $("#err_admission_year").hide();
});
$("#gender").change(function () {
    $("#err_gender").hide();
});
$("#password").keyup(function () {
    $("#err_password").hide();
    $("#err_password_valid").hide();
    $("#err_confirm_password_not_match").hide();
});
$("#confirm_password").keyup(function () {
    $("#err_confirm_password").hide();
    $("#err_confirm_password_not_match").hide();
});
$("#agree").change(function () {
    $("#err_agree_terms_and_conditions").hide();
});





function Register() {
    var emailfilter = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
    var passwordfilter = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/
    var registered_as = $("#registered_as").val();
    var registered_as_text = $("#registered_as option:selected").text();
    var first_name = $("#first_name").val();
    var middle_name = $("#middle_name").val();
    var last_name = $("#last_name").val();
    var email = $("#email").val();
    var phone_no = $("#phone_no").val();
    var course = $("#course").val();
    // var specialization = $("#specialization").val();
    var admission_year = $("#admission_year").val();
    var gender = $("#gender").val();
    var semesters = $("#semesters").val();
    var sections = $("#sections").val();
    var password = $("#password").val();
    var confirm_password = $("#confirm_password").val();
    if (registered_as == "") {
        $("#err_registered_as").show();
    } else if (first_name == "") {
        $("#err_first_name").show();
    }
    // else if(middle_name == ""){
    //     $("#err_middle_name").show();
    // }
    else if (last_name == "") {
        $("#err_last_name").show();
    } else if (email == "") {
        $("#err_email").show();
    } else if (!emailfilter.test(email)) {
        $("#err_email_valid").show();
    } else if (password == "") {
        $("#err_password").show();
    } else if (!passwordfilter.test(password)) {
        $("#err_password_valid").show();
    } else if (confirm_password == "") {
        $("#err_confirm_password").show();
    } else if (password != confirm_password) {
        $("#err_confirm_password_not_match").show();
    }else if (phone_no == "") {
        $("#err_phone_no").show();
    } else if (phone_no.length < 10) {
        $("#err_phone_no_valid").show();
    } else if (gender == "") {
        $("#err_gender").show();
    }
    // else if(specialization == ""){
    //     $("#err_specialization").show();
    // }
     else if (registered_as_text == "Student" && course == "") {
        $("#err_course").show();
    } else if (registered_as_text == "Student" && semesters == "") {
        $("#err_semesters").show();
    } else if (registered_as_text == "Student" && sections == "") {
        $("#err_sections").show();
    } else if (registered_as_text == "Student" && admission_year == "") {
        $("#err_admission_year").show();
    } else if ($("#agree").prop('checked') == false) {
        $("#err_agree_terms_and_conditions").show();
    } else {
        $.ajax({
            method: "POST",
            url: "/Register_user/",
            data: {
                "registered_as": registered_as,
                "registered_as_text": registered_as_text,
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "email": email,
                "phone_no": phone_no,
                "course": course,
                // "specialization" : specialization,
                "admission_year": admission_year,
                "semesters": semesters,
                "sections": sections,
                "gender": gender,
                "password": password
            },
            success: function (response) {
                console.log(response)
                if (response['status'] == "0") {
                    if (response['msg'] == "Email Already Exists") {
                        $("#err_email_already").show();
                    } else {
                        $("#err_phone_no_already").show();
                    }
                } else {
                    swal({
                        title: "Application is under Process",
                        text: "You will get a confirmation Email after successfull authentication.",
                        icon: "success",
                        button: "Ok",
                        closeOnClickOutside: false,
                    }).then(function () {
                        location.href="/login/";
                    });
                }
            }
        })
    }
}
$("#id_username").keyup(function () {
    $("#err_id_username").hide();
    $("#err_invalid_credentials").hide();
    $("#err_unauthorized_user").hide();
});
$("#id_password").keyup(function () {
    $("#err_id_password").hide();
    $("#err_invalid_credentials").hide();
    $("#err_unauthorized_user").hide();
});






function signin() {
    var emailfilter = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
    var id_username = $("#id_username").val();
    var id_password = $("#id_password").val();
    if (id_username == "") {
        $("#err_id_username").show();
    } else if (!emailfilter.test(id_username)) {
        $("#err_id_username_invalid").show();
    } else if (id_password == "") {
        $("#err_id_password").show();
    } else {
        $.ajax({
            method: "POST",
            url: "/Signup_user/",
            data: {
                "id_username": id_username,
                "id_password": id_password
            },
            success: function (response) {
                console.log(response)
                if (response == "error") {
                    $("#err_invalid_credentials").show();
                } else if (response == "unauthorized user") {
                    $("#err_unauthorized_user").show();
                } else {
                    location.href = "/Profile_user/"
                }
            }
        })
    }
}
$("#input_forget_password").keyup(function () {
    $("#err_forgetpassword_email").hide();
    $("#err_forgetpassword_email_invalid").hide();
    $("#email_not_exists_forgetpassword").hide();
});




function forget_password() {
    var emailfilter = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i;
    var input_forget_password = $("#input_forget_password").val();
    if (input_forget_password == "") {
        $("#err_forgetpassword_email").show();
    } else if (!emailfilter.test(input_forget_password)) {
        $("#err_forgetpassword_email_invalid").show();
    } else {
        $.ajax({
            method: "POST",
            url: "/ForgotPassword/",
            data: {
                "input_forget_password": input_forget_password
            },
            success: function (response) {
                if (response['status'] == "0") {
                    $("#email_not_exists_forgetpassword").show();
                } else {
                    $('#ForgetPassword_Modal').modal('hide');
                    $("#input_forget_password").val("");
                    swal({
                        text: response['msg'],
                        icon: "success",
                        button: "Ok"
                    });
                }
            }
        })
    }
}