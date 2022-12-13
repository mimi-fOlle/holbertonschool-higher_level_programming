const url = "https://stefanbohacek.com/hellosalut/?lang=fr";

$(function () {
    $.get(url, function (data) {
        $("DIV#hello").text(data.hello);
    });
});