document.createSvg = function(tagName) {
        var svgNS = "http://www.w3.org/2000/svg";
        return this.createElementNS(svgNS, tagName);
    };
    
    var numberPerSide = 20;
    var size = 10;
    var pixelsPerSide = 400;
    
    
    
    var grid = function(numberPerSide, size, pixelsPerSide, color,coor,data,hide_flag,current_step) {
	var svg = document.createSvg("svg");
        svg.setAttribute("width", pixelsPerSide);
        svg.setAttribute("height", pixelsPerSide);
        svg.setAttribute("viewBox", [0, 0, numberPerSide * size, numberPerSide * size].join(" "));
        for(var i = 0; i < numberPerSide; i++) {
            for(var j = 0; j < numberPerSide; j++) {
              var g = document.createSvg("g");
              g.setAttribute("transform", ["translate(", i*size, ",", j*size, ")"].join(""));

              var number = numberPerSide * j + i;

              var box = document.createSvg("rect");
	    
              if(data[number].SHIPVALUE=="0") { //o trong khong co gi
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","white");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }
	     
              if(data[number].SHIPVALUE=="SELECT" && hide_flag=="false") { //duoc chon, khong che -> khung do
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","red");
                box.setAttribute("stroke-width","5");
                box.setAttribute("rx","20");
                box.setAttribute("ry","20");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }

              if(data[number].SHIPVALUE=="SELECT" && hide_flag=="true" && current_step==1) { //duoc chon, bi che, picking -> hien thi o trong
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","white");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }

              if(data[number].SHIPVALUE=="SELECT" && hide_flag=="true" && current_step==2) { //duoc chon, bi che, picking -> hien thi o trong
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","red");
                box.setAttribute("stroke-width","5");
                box.setAttribute("rx","20");
                box.setAttribute("ry","20");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }

              if(data[number].SHIPVALUE=="SHIP" && hide_flag=="true") {//co thuyen, che
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","white");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }

              if(data[number].SHIPVALUE=="SHIP+SELECT" && hide_flag=="true" && current_step==1) {//co thuyen, duoc chon, che, picking
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","white");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }

              if(data[number].SHIPVALUE=="SHIP+SELECT" && hide_flag=="true" && current_step==2) {//co thuyen, duoc chon, che, playing
                box.setAttribute("width", size);
                box.setAttribute("height", size);
                box.setAttribute("fill", color);
                box.setAttribute("stroke","red");
                box.setAttribute("stroke-width","5");
                box.setAttribute("rx","20");
                box.setAttribute("ry","20");
                box.setAttribute("id", "b" + number);
                g.appendChild(box);
              }
              
              var img = document.createSvg("image");

              if(data[number].SHIPVALUE=="FIRE+SELECT") { //bi ban duoc chon
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "fire-select.png");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }

              if(data[number].SHIPVALUE=="X+SELECT") { //miss duoc chon
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "X-select.png");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }

              if(data[number].SHIPVALUE=="SHIP" && hide_flag=="false") {//co thuyen, ko che
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "ship.jpg");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }

              
              
              if(data[number].SHIPVALUE=="FIRE") {//bi ban
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "fire.jpg");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }
              
              
              if(data[number].SHIPVALUE=="X") {//X
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "X.png");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }
              
              if(data[number].SHIPVALUE=="SHIP+SELECT" && hide_flag=="false") { //co thuyen duoc chon
                img.setAttribute("width", size);
                img.setAttribute("height", size);
                img.setAttribute("href", "ship-select.jpg");
                img.setAttribute("id", "b" + number);
                g.appendChild(img);
              }
              
              svg.appendChild(g);
            }  
        }
        svg.addEventListener(
            "mouseover",
            function(e){
                var id = e.target.id;
                if(id)
                    document.getElementById(coor).innerHTML="x= " + id.substring(1)%numberPerSide + "   y= " + parseInt(id.substring(1)/numberPerSide);
            },
            false);
        /* con tro chuot ra ngoai o
        svg.addEventListener(
            "mouseout",
            function(e){
                var id = e.target.id;
                if(id)
                    document.getElementById(coor).innerHTML="";
            },
            false);
        */
        return svg;
    };