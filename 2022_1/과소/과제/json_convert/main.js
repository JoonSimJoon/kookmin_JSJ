const Infofile= require('./Info.json'); 
let idx=0;
var JsonList = new Array();
Infofile.forEach(images => {
    var max_diagonal = -1;
    var min_diagonal = -1;
    var avr_diagonal = parseFloat(0);
    var boxobject = new Object();
    var idxx=0;
    images.forEach( element=>{
       
        const [bbox,score,cls] = element;
        if(cls==1){
            //console.log(Math.floor((bbox[3]-bbox[1])*100),Math.floor((bbox[2]-bbox[0])*100),score,cls,idx);
            if((bbox[3]-bbox[1]) < (bbox[2]-bbox[0])){
                boxobject.w_bx = ((bbox[3]-bbox[1])*100).toFixed(2);
                boxobject.h_bx = ((bbox[2]-bbox[0])*100).toFixed(2);
                
            }else{
                boxobject.h_bx = ((bbox[3]-bbox[1])*100).toFixed(2);
                boxobject.w_bx = ((bbox[2]-bbox[0])*100).toFixed(2);
            }
            boxobject.w_px = (180/parseFloat(boxobject.w_bx)).toFixed(2);
            boxobject.h_px = (390/parseFloat(boxobject.h_bx)).toFixed(2);
            boxobject.d_px = Math.hypot(boxobject.w_px,boxobject.h_px).toFixed(2)
        }else{
            var data = new Object();
            if((bbox[3]-bbox[1]) < (bbox[2]-bbox[0])){
                data.width = ((bbox[3]-bbox[1])*100).toFixed(2);
                data.height = ((bbox[2]-bbox[0])*100).toFixed(2);
            }else{
                data.width = ((bbox[3]-bbox[1])*100).toFixed(2);
                data.height = ((bbox[2]-bbox[0])*100).toFixed(2);
            }
            data.diagonal =Math.hypot(data.width,data.height).toFixed(2);
            //console.log(data.width, data.height, (data.diagonal));
            if(max_diagonal == -1){
                max_diagonal = data.diagonal;

            }else if(max_diagonal<data.diagonal){
                max_diagonal = data.diagonal;
            }
            if(min_diagonal == -1){
                min_diagonal = data.diagonal;

            }else if(min_diagonal>data.diagonal){
                min_diagonal = data.diagonal;
            }
        }
        if(cls==2){
            boxobject[idxx] = data;
            avr_diagonal+=parseFloat( data.diagonal);
            idxx+=1
        } 
    });
    //console.log(boxobject)
    boxobject.max = max_diagonal;
    boxobject.min = min_diagonal;
    boxobject.num = idxx;
    boxobject.avr = (avr_diagonal/idxx).toFixed(2);
    JsonList.push(boxobject)
    idx+=1;
});
console.log(JsonList[0])
JsonList.forEach(obj=>{
    var n = obj.num;
    for( let i=0;i<n;i++){
        obj[i].width =(obj[i].width *  obj.w_px/10).toFixed(2);
        obj[i].height = (obj[i].height * obj.h_px/10).toFixed(2);
        obj[i].diagonal =(obj[i].diagonal* obj.d_px/10).toFixed(2);
        
    }
    //console.log(obj[0])
    obj.max = (obj.max*obj.d_px/10).toFixed(2);
    obj.min = (obj.min*obj.d_px/10).toFixed(2);
    obj.avr = (obj.avr*obj.d_px/10).toFixed(2);
    
})

console.log(JsonList)