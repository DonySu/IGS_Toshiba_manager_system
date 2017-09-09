function timer(){
    dt = new Date();
    var h = dt.getHours();
    var m = dt.getMinutes();
    var s = dt.getSeconds();
    
    var year = dt.getFullYear();
    var month = dt.getMonth()+1;
    var date = dt.getDate();
    var weekday = dt.getDay();
    
    if (h<10){
        h = "0"+h;
    }
     if (m<10){
        m = "0"+m;
    }
     if (s<10){
        s = "0"+s;
    }
    if (month<10){
        month = "0"+month;
    }
    if (date<10){
        date = "0"+date;
    }
    
    switch(weekday){
        case 0:
            weekday = 'Sun';
            break;
        case 1:
            weekday = 'Mon';
            break;
        case 2:
            weekday = 'Tue';
            break;
        case 3:
            weekday = 'Sat';
            break;
        case 4:
            weekday = 'Thu';
            break;
        case 5:
            weekday = 'Fri';
            break;
        case 6:
            weekday = 'Sat';
            break;            
        }
    document.getElementById('timeshow').innerHTML=h+":"+m+":"+s;
    document.getElementById('dayshow').innerHTML=year+"-"+month+"-"+date+" "+weekday;
    //document.write(h);
    window.setTimeout("timer()",1000)
}
