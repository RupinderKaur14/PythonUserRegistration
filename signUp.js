function check_form(form) {
                
    var password = document.getElementById("password").value;
    var retype =  document.getElementById("rePassword").value;
    console.log("password:"+password);
    var message = document.getElementById("message");


    if (form !== undefined && password == retype) {
        // Validation succeeded, submit the form
        message.innerHTML = "";
        registerUser();
    } else {
        event.preventDefault();
        message.innerHTML = "Passwords do not match!"
    }

    
}

function registerUser() {
    console.log("Inside register user");
    const  username = document.getElementById('username').value;
    const  password = document.getElementById('password').value;
    var smessage = document.getElementById("successMessage");
    

    var fmessage = document.getElementById("failedMessage");
  
    
    fetch("http://127.0.0.1:5000/user",{
        method: 'POST',
        headers: { 'Content-Type':'application/json'},
        body: JSON.stringify({username, password})
    }).then(response =>{

        if (response.status == 200) {
            fmessage.innerHTML = "";
            smessage.innerHTML = 'User registered successfully.';
        }
        else if (response.status == 401) {
            smessage.innerHTML = "";
            fmessage.innerHTML = 'User already exist.';
        } else {
            smessage.innerHTML = "";
            fmessage.innerHTML = 'Registration failed.';
        }                 
    
    }).catch(error =>{
        console.error("Registration error:",error);
    });
    
}