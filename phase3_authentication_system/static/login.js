// Function to hash a password using SHA-256
async function hashPassword(password) {
    // Encode the password as UTF-8
    const encoder = new TextEncoder();
    const data = encoder.encode(password);

    // Hash the password using SHA-256
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    
    // Convert the hash to a hexadecimal string
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

    return hashHex;
}

async function login(){
    const password = document.getElementById("password").value;
    const hashedPassword = await hashPassword(password);
    const email = document.getElementById("email").value;
    
    login_json_object = {
        "email":email,
        "password":hashedPassword
    }
    
    console.log(login_json_object);
    
    $.ajax({
        url: `http://127.0.0.1:8002/login`,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(login_json_object),

        success: function (response) {
            if (response.message === "Invalid Credentials"){
                alert("Invalid Credentials")
            }
            else if(response.message === "Valid Credentials"){
                alert("Valid Credentials");
                console.log(response.access_token);
                sessionStorage.setItem('access_token', response.access_token);
                window.location.href = response.redirect_link;
                
            }
                

        },
        error: function(error) {
            alert("Some Error Occurred !!!!!")
        }
    });


}

// function determine_user_type() {
//     const token = sessionStorage.getItem('access_token');
//     let payload = null;

//     try {
//         const base64Payload = token.split('.')[1];
//         if (!base64Payload) {
//             console.log("some issue founda");
//         }

//         payload = JSON.parse(window.atob(base64Payload));

//         return payload.user_type;

//     } catch (e) {
//         console.log("Error decoding token:", e);
//         return null;
//     }

    
// }


// function redirect_to_protected_route(user_type){
//     if(user_type === "doctor"){

//     }
//     else if (user_type === "admin"){

//     }

// }