<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title style="text-align: center;">随机</title>
    <style>
        /* 设置网页的背景颜色 */
        body{background-color: cadetblue;}
    </style>
</head>
<body >
    <h1>ssss</h1>
    <!-- 设置网页的标题 -->
    <h1 style="text-align: center;" >随机点名</h1>
    <!-- 设置时间显示位置根据ID再js中调用方法显示 -->
    <div color="#33FFFF" style="text-align: right;"><span id="nowDateTimeSpan" ></span></div><br>     
</body>
<script src="js/jquery-3.3.1.min.js"></script>
<script>
    //定义时间1秒刷新一次
    setInterval(function time(){
       let time1 =new Date
      let time=time1.toLocaleString()
       document.getElementById("nowDateTimeSpan").innerHTML=time
    },1000)
    //定义数组存储名单
    var student = "张三,李四,王五,赵六,吴七,陈麻子";
   var arrs =student.split(",")
    
    //创建表格并赋值
    var j =0;
    htmlstr="<table border=0  align=center cellspacing=10 cellpadding=3>"
        htmlstr+="<tr>"
        //进行循环创建表格 每排9个表格，根据arrs数组个数创建
        for(j;j<=arrs.length-1;j++){
            if(j%9==0){
                htmlstr+="<tr>"
            }
            htmlstr+="<td   name=strtd align=center bgcolor=cyan>"+arrs[j]+"<td>"
        }
        htmlstr+="<tr>"
    htmlstr+="</table >"
        document.write(htmlstr)
    
    //设置一个arrs数组长度的随机数
    function rand(){
       let rand= Math.random()  
            return rand2=Math.floor(rand*arrs.length-1) 
    }
    rand();
    //绑定事件
        //开始事件
     function kaishi(){
         //获取开始按钮并且通过disabled来禁用多次点击
         var dis=document.getElementById("input1")
            dis.setAttribute("disabled","disabled")
            //检查是否存在已经选定的表格根据是否存在ID来选择
        var reds =document.getElementById("reds")
        //如果存在已经变色的表格就将其变回来然后删除ID
        if(reds!=null){
            reds.setAttribute("bgcolor","cyan")
            reds.removeAttribute("id")
        }
        //获取所有的表格元素组成数组
         var td =document.getElementsByName("strtd")
         //定义一个循环事件 ，随机表格颜色变色
          one= setInterval(function(){
             var ran=rand()
             td[ran].setAttribute("bgcolor","red")
            setTimeout(function(){
             td[ran].setAttribute("bgcolor","cyan")
            },100)
          },100)
    }
        //停止事件
    function tingzhi(){
        //先查找是否存在已经变色的表格
        var reds1 =document.getElementById("reds")
        //如果存在就停止开始按钮
        if(reds1==null){
       clearInterval(one)
       //同时解除开始按钮的禁用状态
       var dis=document.getElementById("input1")
            dis.removeAttribute("disabled")
            //进行最后一次随机选定一个表格变色并且给该表格添加ID元素并且赋值
       var td =document.getElementsByName("strtd")
          one= setTimeout(function(){
             var ran=rand()
             td[ran].setAttribute("bgcolor","red")
             td[ran].setAttribute("id","reds")
          },1)
        }else{
            //如果存在一个选定的变色表格就说明尚未开始 发出弹窗提示
            alert("请点击开始后再停止")
        }
    }
</script>
<body>
    <!-- 创建按钮 -->
    <table style="table-layout: fixed;"  width="100%" height="100%" cellspacing="0" cellpadding="2">
        <tr></tr>
        <tr>
            <td align="center" >
                <input id="input1"  onclick="kaishi()"  type="button" value="开始"  >
                <input id="input2" onclick="tingzhi()"  type="button" value="停止"  >
            </td>
        </tr>
    </table>
</body>
</html>
