var a = document.getElementById("koffer-svg");
// I10

// It's important to add an load event listener to the object,
// as it will load the svg doc asynchronously
a.addEventListener("load",function(){

    var leds = [];
    var kippschalter = [];

    var svgDoc = a.contentDocument;

    var led_O0 = svgDoc.getElementById("LED_O0"); 
    var led_O1 = svgDoc.getElementById("LED_O1");
    var led_O2 = svgDoc.getElementById("LED_O2");
    var led_O3 = svgDoc.getElementById("LED_O3");
    var led_O4 = svgDoc.getElementById("LED_O4");
    var led_O5 = svgDoc.getElementById("LED_O5");
    var led_O6 = svgDoc.getElementById("LED_O6");
    var led_O7 = svgDoc.getElementById("LED_O7");
    var led_O8 = svgDoc.getElementById("LED_O8");
    var led_O9 = svgDoc.getElementById("LED_O9");
    var led_O10 = svgDoc.getElementById("LED_O10");

    var kippschalter_I6 = svgDoc.getElementById("I6");
    var kippschalter_I7 = svgDoc.getElementById("I7");
    var kippschalter_I8 = svgDoc.getElementById("I8");
    var kippschalter_I9 = svgDoc.getElementById("I9");
    var kippschalter_I10 = svgDoc.getElementById("I10");

    leds.push(led_O0,led_O1,led_O2,led_O3,led_O4,led_O5,led_O6,led_O7,led_O8,led_O9,led_O10);
    console.log("leds", leds);
    kippschalter.push(kippschalter_I6,kippschalter_I7,kippschalter_I8,kippschalter_I9,kippschalter_I10);

    console.log("kipp", kippschalter_I10);
    kippschalter_I10.childNodes.forEach(function(e) {
        if(e.id && e.id.startsWith("flipped")) {
            e.style.display = "none"
        }
    });


    // Add Eventlistener
    kippschalter.forEach(function(e) {
        e.addEventListener('click', function (event) {
            console.log("click", e);
            e.childNodes.forEach(function(elem) {
                if(elem.id && elem.id.startsWith("flipped")) {
                    elem.style.display = "block"
                } else if (elem.id) {
                    elem.style.display = "none"
                }
            });
        }, false);
        e.addEventListener('mouseover', function (event) {
            e.style.cursor = "pointer"; 
        });
        e.addEventListener('mouseout', function (event) {
            e.style.cursor = "default"; 
        });

    });

    console.log("LED_O0", led_O0);
    led_O0.style.fill = "blue";
    led_O1.style.fill = "blue";
    led_O2.style.fill = "blue";
    led_O3.style.fill = "blue";
    led_O4.style.fill = "blue";
    led_O5.style.fill = "blue";
    led_O6.style.fill = "blue";
    led_O7.style.fill = "blue";
    led_O8.style.fill = "blue";
    led_O9.style.fill = "blue";
    led_O10.style.fill = "blue";


}, false);