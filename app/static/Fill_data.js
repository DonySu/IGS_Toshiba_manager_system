function fill_data()
{

    var old_data = document.getElementsByClassName("old"); 
    old_password = old_data[0].innerHTML; 
    old_email = old_data[1].innerHTML;
    old_phone = old_data[2].innerHTML;
    old_section = old_data[3].innerHTML;
    old_user_img = old_data[4].innerHTML;

    var input_phone = document.getElementsByName("phone");
    input_phone[0].value = old_phone;

    var input_email = document.getElementsByName("email");
    input_email[0].value = old_email;
 
    var input_password = document.getElementsByName("password");
    var input_confirm = document.getElementsByName("confirm");
    input_confirm[0].value = old_password;
    input_password[0].value = old_password;
 
    var input_select = document.getElementsByTagName("select");
    var section_option_select = input_select[0].childNodes;
    for (i=0;i<6;i++){
        
        if (section_option_select[i].getAttribute("value")== String(old_section).toLowerCase()){
            section_option_select[i].setAttribute("selected","selected");
        }
    }
    var img_option_select = input_select[1].childNodes;
    len = String(old_user_img).length;
    string1 = String(old_user_img)[0];
    string2 = '';
    for (i=1;i<len;i++){
        string2 += String(old_user_img)[i].toLowerCase();
    }
    img_compare_string = string1 + string2;
    for (i=0;i<6;i++){
        
        if (img_option_select[i].getAttribute("value")== img_compare_string){
            img_option_select[i].setAttribute("selected","selected");
        }
    }
 }
    

