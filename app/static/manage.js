/*该程序文件中默认每页最大显示为10，如果该数值被修改，该文件应该被同步修改*/

function show_add(){
    area_add = document.getElementsByClassName("manage_list_add_area")[0];
    area_edit = document.getElementsByClassName("manage_list_edit_area")[0];
    area_add.style.display = "block";
    area_edit.style.display = "none";
    //alert("Add选中");
}

function show_edit(){
    area_add = document.getElementsByClassName("manage_list_add_area")[0];
    area_edit = document.getElementsByClassName("manage_list_edit_area")[0];
    area_add.style.display = "none";
    area_edit.style.display = "block";

    checkbox_checked= new Array();
    checkbox_edit = new Array();
    len = document.getElementsByName("checkbox").length;
    
    id_max = document.getElementsByName("checkbox")[0].getAttribute("id");
    //alert(id_max);
    if (id_max <= 10){
        page_num = 1;
        //alert(page_num);
    }
    else{
        temp = Math.ceil(id_max/10);/*向上取整*/
        //alert(temp);
        page_num = temp;
        //alert(page_num);
    }
    
    for(i=0;i<len;i++){
        if(document.getElementsByName("checkbox")[i].checked){
            checkbox_checked.push(document.getElementsByName("checkbox")[i].getAttribute("id"));
            checkbox_edit.push(len-i);
        }
    }
    //alert(checkbox_edit);
    if (checkbox_checked.length==0){
        //alert(checkbox_checked.length);
        alert("请选择一项进行编辑");
        document.location.href="http://127.0.0.1:5000/manage/"+page_num;
    }
    else if(checkbox_checked.length > 1){
        alert("请不要选择多项");
        document.location.href="http://127.0.0.1:5000/manage/"+page_num;
    }
    else{
        //alert("选中："+checkbox_checked);
        document.getElementById(checkbox_checked).setAttribute("checked","True");
        document.location.href="http://127.0.0.1:5000/edit_notice/"+page_num+":"+checkbox_checked+":"+checkbox_edit;        
    }
}


function show_checkbox(){
    checkbox_checked= new Array();
    max_id = document.getElementsByName("checkbox")[0].getAttribute("id");
    current_page = Math.ceil(max_id/10);/*向上取整*/
    
    len = document.getElementsByName("checkbox").length;
    for(i=0;i<len;i++){
        if(document.getElementsByName("checkbox")[i].checked){
            checkbox_checked.push(document.getElementsByName("checkbox")[i].getAttribute("id"));
        }
    }
    
    if (checkbox_checked.length==0){
        //alert(checkbox_checked.length);
        alert("没有项目选中,请重新选择");
        document.location.href="http://127.0.0.1:5000/manage/"+current_page;
    }
    else{
        //alert("选中："+checkbox_checked);
        document.location.href="http://127.0.0.1:5000/delete_notices/"+checkbox_checked;
    }
}

function edit_confirm(){
    temp_old = document.getElementsByClassName("old");
    //alert(temp_old[0].innerHTML);
    //alert(temp_old[1].innerHTML);
    //alert(temp_old[2].innerHTML);
    document.getElementById("title_edit").setAttribute("value",temp_old[0].innerHTML);
    document.getElementById("content_edit").value=temp_old[1].innerHTML;
    
    child = document.getElementById("species_edit").childNodes;
    for (i=0;i<child.length;i++){
        if (child[i].getAttribute("value") == temp_old[2].innerHTML){
            child[i].setAttribute("checked");
        }
        
    }
    
}