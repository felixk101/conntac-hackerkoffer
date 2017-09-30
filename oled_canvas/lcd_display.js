
var canvas = document.getElementById("lcd_canvas");
var ctx = canvas.getContext("2d");

function drawPixel(x, y, onoff) {
    var multiplier_x = canvas.offsetWidth / 128;
    var multiplier_y = canvas.offsetHeight / 64;

    ctx.fillStyle = onoff ? "black" : "white";

    ctx.rect(x * multiplier_x, y * multiplier_y,
             multiplier_x, multiplier_y);

    ctx.fill();
}

function updateCanvas() {
    drawPixel(0, 0, true);

    console.log("Updated canvas")
}
