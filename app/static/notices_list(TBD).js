function show_notices_list(){
    var init_node = document.getElementsByClassName("notices_list_table")[0];
    /*alert(init_node.innerHTML);
    init_node.innerHTML="AAAAA";*/
    var new_tr_node = document.createElement("tr");
    
    var new_td_node_type = document.createElement("td");
    new_td_node_type.className="notices_list_table_type";
    var new_td_node_title = document.createElement("td");
    new_td_node_title.className="notices_list_table_title";
    var new_td_node_author = document.createElement("td");
    new_td_node_author.className="notices_list_table_author";
    var new_td_node_create_date = document.createElement("td");
    new_td_node_create_date.className="notices_list_table_create_date";
    
    init_node.appendChild(new_tr_node);
    td1=init_node.appendChild(new_tr_node).appendChild(new_td_node_type);
    td2=init_node.appendChild(new_tr_node).appendChild(new_td_node_title);
    td3=init_node.appendChild(new_tr_node).appendChild(new_td_node_author);
    //td3.innerHTML = '123456';
    td4=init_node.appendChild(new_tr_node).appendChild(new_td_node_create_date);
    //td4.innerHTML = '123456';
    //alert(document.getElementsByClassName("notices_list_type").length)
}
        