function tabs_find()
{
    var find_tabs = document.getElementsByClassName('manage_tab');
    
    var find_tabs_input = find_tabs[0].getElementsByTagName('input');
    
    for (var i=0; i<find_tabs_input.length; i++){
        
        find_tabs_input[i].onclick = function(){
            //alert("点中按钮");
            for(var j=0; j<find_tabs_input.length;j++){
                find_tabs_input[j].style.borderBottom='';
                find_area_str = "manage_tab_area_"+(j+1);
                //alert(find_area_str);
                find_tabs_area = document.getElementsByClassName(find_area_str)[0];
                find_tabs_area.style.display="none";
            }
            this.style.borderBottom="2px solid red";
            div_index=this.getAttribute("id")[11];
            find_area_str_now = "manage_tab_area_"+div_index;
            //alert(find_area_str_now);
            find_tabs_area_now = document.getElementsByClassName(find_area_str_now)[0];
            find_tabs_area_now.style.display="block";
            
            /*if (div_index == 1){
                to_set_id = document.getElementById("manage_tab_area_1_form");
                to_set_id.action = "/manage/"+div_index;
            }
            
            if (div_index == 2){
                to_set_id = document.getElementById("manage_tab_area_2_form");
                to_set_id.action = "/manage/"+div_index;
            }*/
            
         }
        
     }
}
//第一个For循环为往各个input标签下添加onclick绑定的function
//第二个for循环为在某个tab被选中后，先将各个input标签以及对应的显示块初始化
