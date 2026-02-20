
// this function prints hello world when the user on click the button element on html
function printHelloWorld(){
    let print_content = document.getElementById("user_password_input");

    // if the password is correct, it prints out that the user got the correct password
    if (print_content.value == "password"){
        console.log("you got the password correct!");
    }
}